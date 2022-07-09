import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    pos=0
    neg=0
    zero=0

    for i in range(len(arr)):
        if(arr[i]>0):
            pos+=1
        elif(arr[i]<0):
            neg+=1
        else:
            zero+=1
            
    print("{0:.6f}".format(pos/len(arr))) 
    print("{0:.6f}".format(neg/len(arr)))   
    print("{0:.6f}".format(zero/len(arr)))          

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)