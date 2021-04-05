# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:18:57 2021

@author: girisairam.ragam
"""

arr= [2,5,40,60,60,10,20]
arr_len = len(arr)
def InsertionSort(arr,arr_len):
    for i in range(1,arr_len):
        key = arr[i]
        j=i-1
        while(j>=0 and arr[j] > key):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
InsertionSort(arr,arr_len)
print(arr)