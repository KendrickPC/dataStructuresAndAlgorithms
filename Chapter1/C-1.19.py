# -*- coding: utf-8 -*-

# Demonstrate how to use Python’s list comprehension syntax to produce
# thelist[ a , b , c ,..., z ],but without having to type all 26 such
# characters literally.

# Hint: Use the chr function with appropriate range
# 2 Chapter 1. Python Primer

print ','.join([chr(int(x)) for x in range(97, 123)])

