"""R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n."""
def oddsum(n):
    return sum([ i**2 for i in range(n) if i%2 == 1])

