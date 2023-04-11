"""R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function."""

def squaressum02(n = int):
    return sum([i**2 for i in range(n)])