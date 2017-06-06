# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 18:57:53 2017

@author: Narukurti Kavya
"""
#prime numbers
num=[]
for i in range(100000,110000):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            num.append(i)
            

print len(num)


