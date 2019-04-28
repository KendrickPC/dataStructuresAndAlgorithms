# -*- coding: utf-8 -*-

# Write a short program that takes as input three integers, a, b, and c,
# from the console and determines if they can be used in a correct
# arithmetic formula (in the given order),
# like “a+b = c,” “a = b−c,” or “a∗b = c.”

# Hint: Try a case analysis for each pair of integers and an operator.

def valid(a, b, c):
  if a + b == c:
    return True
  elif a == b - c:
    return True
  elif a * b == c:
    return True
  else:
    return False

print(valid(2, 2, 4))
print(valid(7, 9, 48))