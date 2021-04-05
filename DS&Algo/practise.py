# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 11:28:08 2021

@author: girisairam.ragam
"""
n=5
for x in range(0,n,1):
    print(x)
#----------------------------------------------
c=6
n=20
for x in range(0,n,c):
    print(x)
#---------------------------------------------- 
c=3
n=33
arrayList = []
k=0
while(c**(k)<n):
    arrayList.append(c**k)
    k+=1
print(arrayList)

#-----------------------------------------------
n=81
c=3
k=0
arrayList = []
while(int(n/c**k)>1):
    arrayList.append(int(n/c**k))
    k+=1
print(arrayList)
#------------------------------------------------
n=514
c=3
k=0
arrayList=[]
while(2**c**k <n):
    arrayList.append(2**c**k)
    k=k+1
print(arrayList)