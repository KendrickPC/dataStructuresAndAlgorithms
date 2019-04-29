# -*- coding: utf-8 -*-

# Write a Python program that can take a positive integer greater than
# 2 as input and write out the number of times one must repeatedly divide
# this number by 2 before getting a value less than 2.

# Hint: This is the same as the logarithm, but you can use recursion here
# rather than calling the log function.

def divideByTwo(n):
  k = 0
  while(n >= 2):
    n /= 2
    k += 1
  return k

n = int(raw_input("Enter an integer:\n"))
print(divideByTwo(n))
