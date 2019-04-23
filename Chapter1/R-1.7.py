# Give a single command that computes the sum from Exercise R-1.6, relying on
# Pythons comprehension syntax and the built-in sum function.

def sq_sum_odd(n):
  return sum([k * k for k in range(0, n) if k % 2 != 0])

print(sq_sum_odd(input("Input an integer:\n")))
