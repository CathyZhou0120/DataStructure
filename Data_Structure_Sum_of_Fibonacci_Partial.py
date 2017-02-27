# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:23:41 2017

@author: Yanran.Zhou
"""


from numpy import empty
import sys

def calc_fib(n):
    if n <= 1:
        return(n)
    else:
        arr = empty(n+1,dtype=object)
        arr[0] = 0
        arr[1]=1
        for i in range(2,n+1):
            arr[i]=arr[i-1]+arr[i-2]
        return(arr[n])
        
    

def calc_fib_sum_partial(n,m):
    if n <= 1 and m<=1 and m>n:
        arr_l = []
        arr_l.append(m)
        return(sum(arr_l))
    elif n == 1 and m == 1:
        arr_l_m = []
        arr_l_m.append(n)
        return(sum(arr_l_m))
    elif n == m and n >1:
        arr_l_2 = []
        arr_l_2.append(calc_fib(n))
        return (sum(arr_l_2))
    elif n!= m and n< m and n > 1 and m >1:
        arr_sum =  []
        for i in range(n,m+1):
            arr_sum.append(calc_fib(i))
        return(sum(arr_sum))




sum_str = str(calc_fib_sum_partial(10,200))
print(sum_str[len(sum_str)-1])    