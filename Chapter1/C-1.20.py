# -*- coding: utf-8 -*-

# Python’s random module includes a function shuffle(data) that accepts a list of
# elements and randomly reorders the elements so that each possible order
# occurs with equal probability. The random module includes a more basic function
# randint(a, b) that returns a uniformly random integer from a to b (including
# both endpoints). Using only the randint function, implement your own version of
# the shuffle function.

# Hint: Consider randomly swapping an element to the first position,
# then randomly swapping a remaining element to the second position, and
# so on.

from random import randint
def shuffle(seq):
  # Shuffle function of random
  l = []
  while (len(seq) > 0):
    r = randint(0, len(seq)-1)
    l += [seq[r]]
    del seq[r]
  print(l)
