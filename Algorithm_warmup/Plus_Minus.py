#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p_count,n_count,z_count,arr_length = 0,0,0,len(arr)
    for i in arr:
        if i >0:
            p_count+=1
        elif i<0:
            n_count+=1
        else:
            z_count+=1
    print("{} \n {} \n {}".format((p_count/arr_length),(n_count/arr_length),(z_count/arr_length)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
