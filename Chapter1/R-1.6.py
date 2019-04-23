# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

# Hint: Consider modifying the range over which you loop.

def sum_of_squares_odd(n):
  n -= 1
  total = 0
  while n > 0:
    if n % 2 != 0:
      total += n * n
    n -= 1
  return total

print sum_of_squares_odd(input("Input an integer:\n"))
