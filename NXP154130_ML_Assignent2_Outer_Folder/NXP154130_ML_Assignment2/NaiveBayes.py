'''
Created on Mar 10, 2016

@author: NAVE
'''
import math
def naivebayes_accuracy(positive,negative,negative_attribute_count,positive_attribute_count,wordlist_train,wordcount,wordlist_test,wordpositions,output_list):
    
    i=0
    j=0
    p_of_positive=math.log2(positive/(positive+negative))
    p_of_negative=math.log2(negative/(positive+negative))
    correct_positive=0
    correct_negative=0
    positive_total=0
    negative_total=0
    for list in wordlist_test:
       p_of_positive=positive/(positive+negative)
       p_of_negative=negative/(positive+negative) 
       for words in list:
           try:
              total=wordpositions[i][j]
              
           except:
              total=0
           
           try:
               train_index=wordlist_train.index(words)
               try:
                  positive_total=positive_attribute_count[train_index]+1
               except:
                   positve_total=1 
               try:
                  negative_total=negative_attribute_count[train_index]+1
               except:
                   negative_total=1
               try: 
                  train_total=wordcount[train_index]+len(wordlist_train)+1
               except:
                  train_total=len(wordlist_train)+1
           except:
                positve_total=1
                negative_total=1
                train_total=len(wordlist_train)+1
           p_of_positive=p_of_positive+total*math.log2((positive_total/train_total))
           p_of_negative=p_of_negative+total*math.log2((negative_total/train_total))
           
           j=j+1
       if p_of_positive > p_of_negative:
           value="TRUE"
       else:
           value="FALSE"
        
       if value == output_list[i]:
           correct_positive=correct_positive+1
       else:
           correct_negative=correct_negative+1    
       
       i=i+1
       j=0
    return correct_positive/(correct_negative+correct_positive)