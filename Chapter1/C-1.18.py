# -*- coding: utf-8 -*-

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

# Hint: What are the factors of each number? Pronic numbers.

# https://stackoverflow.com/questions/25077095/what-is-a-clearer-way-to-generate-this-sequence-of-numbers

pronicList = [x*(x + 1) for x in range(10)]
print pronicList

