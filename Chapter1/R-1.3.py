# Write a short Python function, minmax(data), that takes a sequence of one
# or more numbers, and returns the smallest and largest numbers, in the form
# of a tuple of length two. Do not use the built-in functions min or max in 
# implementing your solution.

# Hint: Keep track of the smallest and largest value while looping.

def minmax(data):
  min = data[0]
  max = data[0]
  for numbers in data:
    if min > numbers:
      min = numbers
    elif max < numbers:
      max = numbers
  return min, max

print(minmax([2,3,4,9,6,4,2,1,0]))


