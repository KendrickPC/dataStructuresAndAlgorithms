# -*- coding: utf-8 -*-

# Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it
# returns an array c of length n such that
# c[i] = a[i]·b[i], for i = 0,...,n−1.

# Hint: Go back to the definition of dot product and write a for loop that
# matches it.

a, b, c = [], [], []

i = int(raw_input("Input a length for i:\n")) + 1

for x in range(i):
  a.append(x)
  b.append(x)
  c.append(a[x] * b[x])

print c






