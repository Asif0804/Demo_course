# -*- coding: utf-8 -*-
"""Q9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LMkVQghTKATzzTJ_gXU9wAA5pfkeNjlx
"""

lst1 = [int(item) for item in input("Enter the list items").split()]
d={}
for i in lst1:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
print(d)

