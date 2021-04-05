# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:22:51 2021

@author: girisairam.ragam
"""

arr = [10,5,8,20,2,18]
arr_len =len(arr)

    
def SelectionSort(arr, arr_len):
    arr_new = [None]*arr_len
    for i in range(0, arr_len):
        min_idx = 0
        for j in range(1, arr_len):
          if arr[j] < arr[min_idx]:
              min_idx = j
        arr_new[i] = arr[min_idx]
        arr[min_idx] = float('inf')
    #Copy arr_new to arr
    for i in range(0,arr_len):
        arr[i] = arr_new[i]
        
SelectionSort(arr,arr_len)
print(arr)


def Swap(arr, first_idx , second_idx):
    temp = arr[first_idx]
    arr[first_idx] = arr[second_idx]
    arr[second_idx] = temp
 

arr = [10,5,8,20,2,18]
arr_len =len(arr)
#Optimized interms of not using new array
def SelectionSortOptimized(arr, arr_len):
    for i in range(0, arr_len-1):
        min_idx = i
        for j in range(i+1, arr_len):
            if arr[j] < arr[min_idx]:
                min_idx = j
        Swap(arr,min_idx,i)

SelectionSortOptimized(arr,arr_len)
print(arr)
        
        
        
        
        
        
        
        
        
        
        
        
        
    