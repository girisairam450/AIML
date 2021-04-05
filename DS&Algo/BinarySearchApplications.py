# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:39:06 2021

@author: girisairam.ragam
"""
'''Binary Search '''
def binarySearch(arr, x,low,high):
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


'''Applications'''
'''Index of First Occurence of an elemeent in a Sorted Array'''
 #Iterative Approach
def FOISA(arr, arr_len, x):
    low=0
    high=arr_len-1
    cnt=1
    while(low<=high):
        print('Iteration:',cnt)
        cnt+=1
        mid=int((low+high)/2)
        print("Mid Index:{}, Mid Value:{}".format(mid,arr[mid]))
        if arr[mid] > x:
            high = mid-1
        elif arr[mid] <x:
            low = mid+1
        else:
            if mid==0 or arr[mid-1]!=arr[mid]:
                return mid
            else:
                high = mid-1
    return -1

#Recursive Approach
foisa_r_cnt =1
def FOISA_R(arr, low, high, x):
    global foisa_r_cnt
    print("Recursion Call:", foisa_r_cnt)
    foisa_r_cnt+=1
    
    if (low>high):
        return -1       
    mid=int((low+high)/2)
    print("Mid Index:{}, Mid Value:{}".format(mid,arr[mid]))
    if arr[mid] > x:
        return FOISA_R(arr, low, mid-1, x)
    elif arr[mid] <x:
        return FOISA_R(arr, mid+1, high, x)
    else:
        if mid==0 or arr[mid-1]!=arr[mid]:
            return mid
        else:
            return FOISA_R(arr, low, mid-1, x)
    return -1

arr =[5,5,10,10,10,20,20,30,30,40,50,50]
arr_len = len(arr)
print("--------------FOISA-----------------")
print(FOISA(arr, arr_len,10))
print("--------------FOISA_R-----------------")
print(FOISA_R(arr,0, arr_len-1, 10))

'''Index of Last Occurence of an elemeent in a Sorted Array'''
#Iterative Approach
def LOISA(arr,arr_len, x): 
    low=0
    high=arr_len-1
    cnt=1
    while(low<=high):
        print('Iteration:',cnt)
        cnt+=1
        mid=int((low+high)/2)
        print("Mid Index:{}, Mid Value:{}".format(mid,arr[mid]))
        if arr[mid] > x:
            high = mid-1
        elif arr[mid] <x:
            low = mid+1
        else:
            if mid==arr_len-1 or arr[mid+1]!=arr[mid]:
                return mid
            else:
                low = mid+1
# Recursive Approach
loisa_r_cnt =1
last_idx=None
def LOISA_R(arr,low,high, x):
    global loisa_r_cnt, last_idx
    print("Recursion Call:", loisa_r_cnt)
    #To store array length from first recursion call using high parameter
    if loisa_r_cnt ==1:
        last_idx=high
    loisa_r_cnt+=1
    if(low>high):
        return -1        
    mid=int((low+high)/2)
    print("Mid Index:{}, Mid Value:{}".format(mid,arr[mid]))
    if arr[mid] > x:
        return LOISA_R(arr,low,mid-1, x)
    elif arr[mid] <x:
        return LOISA_R(arr,mid+1,high, x)
    else:
        if mid==last_idx or arr[mid+1]!=arr[mid]:
            return mid
        else:
            return LOISA_R(arr,mid+1,high, x)

arr =[5,5,10,10,10,20,20,30,30,40,50,50]
arr_len = len(arr)
print("--------------LOISA-----------------")
print(LOISA(arr, arr_len,50))
print("--------------LOISA_R-----------------")
print(LOISA_R(arr,0,arr_len-1,50))


'''Number of  Occurences of an elemeent in a Sorted Array'''
def NOSA(arr, arr_len, x):
    foisa_index = FOISA(arr, arr_len, x)
    print("--------------------foisa_index:",foisa_index)
    if foisa_index == -1:
        return 0
    else:
        loisa_index = LOISA(arr,arr_len, x)
        print("---------------------loisa_index:",loisa_index)
        return foisa_index if loisa_index == foisa_index else loisa_index - foisa_index +1

print("--------------NOSA-----------------")
print("Number of Occurences: ",NOSA(arr, arr_len,50))


'''Count no of Ones in a Sorted Binary Array'''
def COBA(arr, arr_len):
    low, high = 0, arr_len-1
    while(low <=high):
        mid = int((low+high)/2)
        if arr[mid]==0:
            low = mid+1
        else:
            if mid==0 or arr[mid-1]==0:
                return arr_len - mid
            else:
                high = mid-1
    return 0
arr =[0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
arr_len = len(arr)
print("--------------COBA-----------------")
print(COBA(arr, arr_len))

'''Perfect Square of a given number'''
def PerfectSquare(num):
    high = int(num/2)
    low=0
    if num==1:
        return 1
    while(low<=high):
        mid = int((low+high)/2)
        if mid*mid == num:
            return mid
        elif mid*mid > num:
            high=mid-1
        else:
            low= mid+1
    return -1
print("--------------PerfectSquare-----------------")
print(PerfectSquare(1))

'''Search element in an Infinite Array'''
def SIA(arr,x):
    if arr[0] == x:
        return 0
    i=1
    while(arr[i]<x):
        i=i*2
    if arr[i] == x:
        return i
    else:
        return binarySearch(arr, x, int(i/2)+1, i-1)
arr= [1,2,5,10,20,40,60,80,100,140,190,300,410,470,540,1020,1150,1209,1398,1467,1589,1699,1814]
print("--------------SIA---------------------------")
print(SIA(arr,140))
        

    
    