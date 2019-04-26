# -*- coding: utf-8 -*-

# Write a Python function that takes a sequence of numbers
# and determines if all the numbers are different from each
# other (that is, they are distinct).

# Hint: The simple solution just checks each number against every other
# one, but we will discuss better solutions later in the book.
# But make sure you don’t compare a number to itself.

# https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.php

def distinct_numbers(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False

sequence1 = [1, 3, 5, 7, 9]
sequence2 = [1, 3, 5, 5, 7, 9]

print(sequence1, distinct_numbers(sequence1))
print(sequence2, distinct_numbers(sequence2))