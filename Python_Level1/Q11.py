# -*- coding: utf-8 -*-
"""Q11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LMkVQghTKATzzTJ_gXU9wAA5pfkeNjlx
"""



a = int(input("Enter a number: "))
d = 0
while a > 0:
  c = a%10
  d = c+d
  a //= 10
print("Sum_digits =", d)

while d >= 10:
  sum = 0
  while d > 0:
    b = d % 10
    sum = sum+b
    d //= 10
print("Final output =", sum)