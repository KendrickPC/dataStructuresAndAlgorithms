# -*- coding: utf-8 -*-

# The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is defined as
# X
# For the special case of p = 2, this results in the traditional Euclidean norm,
# which represents the length of the vector. For example, the Euclidean norm of
# a two-dimensional vector with coordinates (4,3) has a Euclidean norm
# of √42 + 32 = √16 + 9 = √25 = 5. Give an implementation of a function named
# norm such that norm(v, p) returns the p-norm value of v and norm(v) returns the
# Euclidean norm of v. You may assume that v is a list of numbers.


# def norm(v,p):
#   a = 0
#   for i in v:
#     a += i**p
#   b = pow(a,1/p)
#   return b

# norm(3, 4)

def norm(v,p=2):
  sum_sq = 0
  for Vi in v:
    sum_sq += Vi**p
  p_norm = sum_sq**(1/p)
  return p_norm
print(norm([3,4]))
