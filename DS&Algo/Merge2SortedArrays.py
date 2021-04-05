# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:54:21 2021

@author: girisairam.ragam
"""
a = [10,20,50,60,90]
b = [5,50,50]

def MergeSortedArrays(arr1,arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    arr = []
    i,j =0,0
    while(i<arr1_len and j<arr2_len):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while(i<arr1_len):
        arr.append(arr1[i])
        i+=1
    while(j<arr2_len):
        arr.append(arr2[j])
        j+=1
    return arr

print(MergeSortedArrays(a,b))

    