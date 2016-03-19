'''
Created on Mar 9, 2016

@author: NAVE
'''
from FileParsing import training, output_list
from FileParsing_stop_word import training_stop
from FileParsing_test import test
from FileParsing_test_stop_words import test_stop1
from LogisticRegression import formequation
from NaiveBayes import naivebayes_accuracy
from Stop_words import stop_words
from LogisticRegression import calculateaccuracy
import sys

training_ham_folder=sys.argv[1]
training_spam_folder=sys.argv[2]
test_ham_folder=sys.argv[3]
test_spam_folder=sys.argv[4]
Learning_Rate=float(sys.argv[5])
Lamda=float(sys.argv[6])
stop_wrords_file=sys.argv[7]

#training_ham_folder="C:/2/hw2_train/train/ham"
#training_spam_folder="C:/2/hw2_train/train/spam"
#test_ham_folder="C:/2/hw2_test/test/ham"
#test_spam_folder="C:/2/hw2_test/test/spam"
#Learning_Rate=0.1
#Lamda=-6

print('running.......','Running Naive Bayes with out stop words')

weightvector,inputvector,positive,negative,negative_attribute_count,positive_attribute_count,wordlist_train,wordcount,train_output_list=training(training_ham_folder,training_spam_folder)
wordlist_test,wordpositions,output_list,test_attributelist=test(wordlist_train,test_ham_folder,test_spam_folder)


accuracy=naivebayes_accuracy(positive, negative, negative_attribute_count, positive_attribute_count, wordlist_train, wordcount, wordlist_test, wordpositions, output_list)


print('running.......','Running Logistic Regression with out stop words')

weight_matrix=formequation(inputvector, weightvector, train_output_list,0,30,Learning_Rate,Lamda)
lg_accuracy=calculateaccuracy(weight_matrix,test_attributelist,output_list)


print('running.......','Running Naive Bayes with stop words')

stop_word=stop_words(stop_wrords_file)
stop_weightvector,stop_inputvector,stop_positive,stop_negative,stop_negative_attribute_count,stop_positive_attribute_count,stop_wordlist,stop_wordcount,stop_train_output_list=training_stop(stop_word,training_ham_folder,training_spam_folder)
test_wordlist,test_wordpositions,stop_output_list,stop_test_attributelist=test_stop1(stop_word,stop_wordlist,test_ham_folder,test_spam_folder)

accuracy_stop=naivebayes_accuracy(stop_positive,stop_negative,stop_negative_attribute_count,stop_positive_attribute_count,stop_wordlist,stop_wordcount,test_wordlist,test_wordpositions,stop_output_list)



print('running.......','Running Logistic Regression with stop words')

weight_matrix_stop=formequation(stop_inputvector, stop_weightvector, stop_train_output_list,0,30,Learning_Rate,Lamda)
lg_accuracy_stop=calculateaccuracy(weight_matrix_stop,stop_test_attributelist,stop_output_list)


print("naive bayes accuracy", accuracy*100)
print("Logistic Regression accuracy",lg_accuracy*100)
print("naive bayes with stop words accuracy",accuracy_stop*100)
print("Logistic Regression with stop words accuracy",lg_accuracy_stop*100)