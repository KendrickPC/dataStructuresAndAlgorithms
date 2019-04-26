# -*- coding: utf-8 -*-

# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

# Hint: Note that both numbers in the pair must be odd.

# https://www.w3resource.com/python-exercises/python-basic-exercise-150.php

def is_product_odd(numbers):
  for i in range(len(numbers)):
    for j in range(len(numbers)):
      if i != j:
        product = numbers[i] * numbers[j]
        if product & 1:
          return True
          return False

sequence1 = [2, 4, 6, 8]
sequence2 = [1, 3, 5, 7]

print(sequence1, is_product_odd(sequence1))
print(sequence2, is_product_odd(sequence2))
