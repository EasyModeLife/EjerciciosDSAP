"""R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""

def squaressum01(n = int):
    return 0 if n == 0 else (((n-1)*(n)*(2*n-1))/6)

