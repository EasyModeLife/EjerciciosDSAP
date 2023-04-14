"""Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function."""
# el anterior lo hice cumpliendo estas condiciones, así que es lo mismo
def oddsum(n):
    return sum([ i**2 for i in range(n) if i%2 == 1])
