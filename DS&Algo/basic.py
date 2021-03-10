# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:52:08 2021

@author: girisairam.ragam
"""
#----------------No of divisors for a given number-----------------------------
#Regular
def divisors_old(num):
    count = 0
    for i in range(1,num+1):
        print("iteration: ", i)
        if num%i==0:
            count+=1
        print("counter:", count)
    return count
print(divisors_old(25))

'''
Optimized
Time Complexity squareroot(num)
'''
import math
def divisors(num):
    count=0
    for i in range(1, (int)(math.sqrt(num)) + 1):
        print("iteration: ", i)
        if num%i == 0:
            if (num / i == i) : 
                count = count + 1
            else :
                count = count + 2
            print("counter:", count)
    return count
print(divisors(25))

#----------------------------------Range Sum ----------------------------------
a = [-1,2,8,-6,17,10,-5,-3]

def sumOfIndexes(i,j):
    if i==0:
        return arr[j]
    else:
        return arr[j]-arr[i-1]

size = len(a)
arr = [None] * size
for i in range(size):
    if i==0:
        arr[0] = a[0]
    else:
        arr[i] = arr[i-1]+a[i]
print("Cummulative array :", arr)

print(sumOfIndexes(2,4))

#---------------------------------Square Root of a given number ---------------
#Regular time complexity: Square root(n)
def square_root_old(num):
    if num==0:
        return 0
    elif num==2:
        return 1
    for i in range(1, num+1):
        print("iteration: ", i)
        if num/i==i:
            return i
print(square_root_old(0))
''' 
Optimized
Binary search
Time complexity logN base2
'''
def square_root(num):
    low =1
    high = num
    if num==0:
        return 0
    elif num==2:
        return 1
    for i in range(num):
        mid = (int)((high+low)/2)
        print("iteration: ", i)
        print("High: ", high)
        print("Low: ", low)
        print("Mid: ", mid)
        square_val = mid*mid
        if square_val > num:
            high = mid-1
        elif square_val < num:
            low = mid+1
        else:
            return mid
print(square_root(2))          
    
    