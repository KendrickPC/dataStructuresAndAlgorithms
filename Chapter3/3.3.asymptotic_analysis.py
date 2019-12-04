# Asymptotic Analysis

def find_max(data):
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest

# A function that returns the maximum value of a Python list.


print(find_max([1, 2, 3, 4, 5]))
print(find_max([1, 2, 3, 4, 25]))