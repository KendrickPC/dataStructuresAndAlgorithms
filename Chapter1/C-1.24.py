# -*- coding: utf-8 -*-

# Write a short Python function that counts
# the number of vowels in a given character string.

vowelCount = 0
string = "Something with vowels in it."
for x in ['a', 'e', 'i', 'o', 'u']:
  for y in string:
    if x == y:
      vowelCount += 1

print(vowelCount)
