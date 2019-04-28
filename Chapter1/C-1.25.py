# -*- coding: utf-8 -*-

# Write a short Python function that takes a string s, representing
# a sentence, and returns a copy of the string with all punctuation
# removed. For example, if given the string "Let's try, Mike.",
# this function would return "Lets try Mike".

# Hint: Consider each character one at a time.

string = "Let's try, Mike."
punctuation = [ '\'' , ';',',','.','\"', '!']

print([x for x in punctuation])


for x in punctuation:
  string = string.replace(x, "")

print(string)
