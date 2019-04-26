# -*- coding: utf-8 -*-

# In our implementation of the scale function(page25),the body of the loop
# executes the command data[j] *= factor. We have discussed that numeric types
# are immutable, and that use of the *= operator in this context causes the
# creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes
# the actual parameter sent by the caller?

# Hint: Think about the semantics of data[j] = data[j] * factor.

# http://claudiordgz.github.io/GoodrichTamassiaGoldwasser/

def scale(data, factor): 
    for val in data: 
        val ∗= factor 
