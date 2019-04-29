# -*- coding: utf-8 -*-

# Write a Python program that can “make change.”
# Your program should take two numbers as input, one that is a monetary
# amount charged and the other that is a monetary amount given. It should
# then return the number of each kind of bill and coin to give back as
# change for the difference between the amount given and the amount
# charged. The values assigned to the bills and coins can be based on the
# monetary system of any current or former government. Try to design your
# program so that it returns as few bills and coins as possible.

# Greedy Method, Recursion of Change Machine.
# https://interactivepython.org/courselib/static/pythonds/Recursion/DynamicProgramming.html

#   Do all arithmetic with integers to avoid the limitations of
#   floating-point arithmetic.

#   Read in the inputs.  Convert each one to a floating-point number,
#   multiply by 100 to get cents, and convert to an integer.
#   Use a named constant instead of a numeric literal.
CPD = 100  # Cents per dollar
cost = int(CPD * float(raw_input("Enter the cost: ")))
tend = int(CPD * float(raw_input("Enter the tendered amount: ")))

#   Calculate the change.
change = tend - cost

#   Construct a tuple with the possible coin values in cents.
denominations = (10000, 5000 ,2000, 1000, 500, 200, 100, 50, 20, 10, 5, 1)
#   Get the number of elements in the tuple.
ndenominations = len(denominations)
#   Initialize a list of counts per denomination.
coinCount = []
for d in denominations:
    coinCount.append(0)

#   To figure out the coins for the change, start with the largest
#   denomination and work down to the smaller ones.
#   Keep track of how much change is left to count out in the
#   "remaining" variable.
#   For each denomination, as long as remaining is greater than
#   value of the coin, repeat adding 1 to the coin count for that
#   denomination and subtracting the denomination value from
#   remaining.

#   Initialize remaining to the total amount of change.
remaining = change

#   deno is an index variable that keeps track of the current
#   denomination.
deno = 0

#   Loop until either we have given all the change or we have
#   run out of coin denominations to check.
while remaining and deno < ndenominations:
    #   For one denomination, count out coins of that denomination
    #   as long as the remaining amount is greater than the denomination
    #   amount.
    while remaining >= denominations[deno]:
        coinCount[deno] += 1
        remaining -= denominations[deno]
    deno += 1

#   Report the results.
print "Your change is $%.02f"% (float(change) / CPD)
for deno in range(0, ndenominations):
    print "$%02.2f coins:\t" % (float(denominations[deno]) / CPD), coinCount[deno]

if cost > tend:
    print "You still owe:\t$%02.2f" % (float(remaining) / CPD)
elif remaining:
    print "Left over:\t$%02.2f" % (float(remaining) / CPD)

