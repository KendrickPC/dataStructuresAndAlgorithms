# -*- coding: utf-8 -*-

# In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementations,
# from page 41, was the most efficient, but we noted that it did not yield the
# factors in increasing order. Modify the generator so that it reports factors
# in increasing order, while maintaining its general performance advantages.

# Hint: Either buffer the bigger value from each pair of factors, or repeat
# the loop in reverse to avoid the buffer.

'''
The desired result is as follows:
1
2
4
5
8
10
20
25
40
50
100
125
200
250
500
1000
'''

# generator that computes factors
def factors(n): 
  k = 1
  # while k < sqrt(n)
  while k * k < n: 
    if n % k == 0:
      yield k
    k += 1
  # special case if n is perfect square
  if k * k == n: 
    yield k
  k = k - 1
  # while k < sqrt(n)
  while k > 0: 
    if n % k == 0:
      yield n // k
    k -= 1

for i in factors(1000):
  print(i)

