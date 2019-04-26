# -*- coding: utf-8 -*-

# Python’s random module includes a function choice(data) that returns a random
# element from a non-empty sequence. The random module includes a more basic
# function randrange, with parameterization similar to the built-in range
# function, that return a random choice from the given range. Using only the
# randrange function, implement your own version of the choice function.

# Hint: Use randrange to pick the index of the chosen element.

from random import randrange

def choiceFunction(data):
  return data[randrange(len(data))]

print(choiceFunction([1, 2, 3, 4, 5]))

