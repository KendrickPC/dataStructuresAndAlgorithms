# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sumOfSquares(n):
  sumSq = 0
  for x in range(n):
    sumSq += x**2
  return sumSq

print sumOfSquares(input("Enter a positive integer:\n"))
