# R-1.2

# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function cannot
# use the multiplication, modulo, or division operators.

# Hint: Use bit operations.

# Cannot use * % /

def is_even(k):
  b = True
  while(b):
    k -= 2
    if k == 0:
      b = False
      return True
    if k < 0:
      b = False
      return b

k = int(raw_input("Enter an integer to check if it is even:\n"))

print is_even(k)
