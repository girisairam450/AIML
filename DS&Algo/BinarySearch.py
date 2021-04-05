# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:23:28 2021

@author: girisairam.ragam
"""
import random

class Search():
    def __init__(self):
        self.abc =0
        
    @staticmethod
    def binarySearch(arr, x, len_arr):
        low = 0
        high = len_arr - 1
        cnt=1
        while(low<=high):
            print("Iteration:",cnt)
            cnt=cnt+1
            mid = int((low+high)/2)
            if arr[mid] == x:
                return mid
            elif arr[mid]>x:
                high = mid-1
            else:
                low = mid+1
        return -1
    
    @staticmethod
    def binarySearchRecursive(arr,low,high, x):
        if low >= high:
            return -1
        else:
            mid = int((low+high)/2)
            print
            if arr[mid] == x:
                return mid
            elif arr[mid]>x:
                return Search.binarySearchRecursive(arr, low, mid-1, x)
            else:
                return Search.binarySearchRecursive(arr, mid+1, high, x)


arr = list(range(0,16,1))
print(arr)
len_arr = len(arr)
x = 15

print(Search.binarySearch(arr, x, len_arr)) 
print(Search.binarySearchRecursive(arr,0,len_arr,x)) 


        
        
        