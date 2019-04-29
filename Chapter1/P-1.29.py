# -*- coding: utf-8 -*-

# Write a Python program that outputs all possible strings formed by
# using thecharacters c , a , t , d , o ,and g exactly once.

# Hint: There are many solutions. If you know about recursion, the
# easiest solution uses this technique. Otherwise, consider using a list
# to hold solutions. If this still seems to hard, then consider using six
# nested loops (but avoid repeating characters and make sure you allow
# allstring lengths).

import itertools

recursionSet = ['c', 'a', 't', 'd', 'o', 'g']
n = len(list(itertools.permutations(recursionSet)))

print(list(itertools.permutations(recursionSet)))
print(n)

# https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-2.php
