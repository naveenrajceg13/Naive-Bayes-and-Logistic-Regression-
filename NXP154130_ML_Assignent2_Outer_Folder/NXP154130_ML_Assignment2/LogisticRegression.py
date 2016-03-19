'''
Created on Mar 10, 2016

@author: NAVE
'''
import math
from ctypes.wintypes import DOUBLE

def formequation(inputvector,weightvector,outputvector,itt,total,Learning_Rate,Lamda):
    
    product_calc=0
    i=0
    j=0
    w0=0
    gradient=[]
    
    weightmatrix=weightvector[0]
    for each_row in inputvector:
        number_of_paramerts=each_row
        for parameters in each_row:
            product_calc=(inputvector[i][j]*weightmatrix[j])+product_calc
            j=j+1
        try:
            ful_sum=float(math.exp(w0+product_calc))
        except:
            ful_sum=w0+product_calc
        ful_sum_below=ful_sum+1
        output_value=1
        if outputvector[i]=='TRUE':
            output_value=1
        else:
            output_value=0
        gradient.insert(i,output_value-(ful_sum/ful_sum_below))
        i=i+1
        j=0
    
    i=0
    j=0
    sum=0
    
    for each_paramaters in number_of_paramerts:
        
        for eachrow in inputvector:
            
            sum=sum+((inputvector[j][i])*gradient[j])
            j=j+1
        weightmatrix[i]=weightmatrix[i]+(Learning_Rate*sum)-(Learning_Rate*Lamda*weightmatrix[i])
        i=i+1
        j=0
    #print(weightvector)
    if itt<=total:
        formequation(inputvector, weightvector, outputvector,itt+1,total,Learning_Rate,Lamda)
    return weightmatrix
        
def calculateaccuracy(weight_matrix,test_input,test_output):
    
    i=0
    j=0
    class_positive=0
    class_negative=0
    for each_row in test_input:
        sum=0
        for each_col in each_row:
            #print(i,j)
            sum=sum+(weight_matrix[j]*test_input[i][j])
            j=j+1
        if(sum>0):
            value="TRUE"
        else:
            value="FALSE"
        if(value==test_output[i]):
            class_positive=class_positive+1
        else:
            class_negative=class_negative+1
        i=i+1
        j=0
    return class_positive/(class_negative+class_positive)