# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:37:37 2021

@author: girisairam.ragam
"""

arr =[2,7,10,8]
arr_len = len(arr)
def Swap(arr, first_idx , second_idx):
    temp = arr[first_idx]
    arr[first_idx] = arr[second_idx]
    arr[second_idx] = temp
    
def BubbleSort(arr, arr_len):
    cnt = 0
    for i in range(0,arr_len-1):
        for j in range(0,arr_len-i-1):
            print(str(j)+' '+str(j+1))
            cnt+=1
            if arr[j] > arr[j+1]:
                Swap(arr, j, j+1)
        #print(arr)
    print("Iterations: ",cnt)
                
BubbleSort(arr, arr_len)
print(arr)

arr =[2,7,10,8]
def BubbleSortOptimized(arr, arr_len):
    cnt = 0
    for i in range(0,arr_len-1):
        IsSwapped = False
        for j in range(0,arr_len-i-1):
            cnt+=1
            if arr[j] > arr[j+1]:
                Swap(arr, j, j+1)
                IsSwapped = True
        if IsSwapped == False:
            break
    print("Iterations: ",cnt)
BubbleSortOptimized(arr, arr_len)
print(arr)