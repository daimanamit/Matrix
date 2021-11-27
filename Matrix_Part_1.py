##Amit Daiman, Locker Number - 375
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:58:41 2019

@author: ada003
"""
#multiply two matrices
#input 3*3 matrices
A = [[11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]]
B = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
#result 3*3 matrices
C = []
for i in range (len(A)):
    Cii=[]
    for j in range (len(B[0])):
        Ci=[]
        for k in range (len(B)):
            Ci.append(A[i][k] * B [k][j])     
        Cii.append(sum(Ci))
    C.append(Cii)
for r in C:
   print(r)