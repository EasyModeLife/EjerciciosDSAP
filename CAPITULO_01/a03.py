"""R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""

def minmax(data):
    min = max = list[0]
    for i in list:
        if i > max:
            max = i
            continue
        if i < min:
            min = i
    return min,max

