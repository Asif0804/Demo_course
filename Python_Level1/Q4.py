# -*- coding: utf-8 -*-
"""Q4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LMkVQghTKATzzTJ_gXU9wAA5pfkeNjlx
"""

Start = int(input("Enter the Start Number"))
End = int(input("Enter the end Number"))
sum = 0
if Start > End:
  print("Invalid number")
for i in range(Start, End+1):
  if i%2 !=0:
    sum = i+sum
print(sum)