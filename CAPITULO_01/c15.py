"""C-1.15 Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)."""

def compare(seq = iter):
    for i in range(len(seq)-1):
        if seq[i] in seq[i+1:]:
            return True
    return False
