"""Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd."""


def oddproduct(lst=list):
    bo = 0
    for i in lst:
        if i%2 == 1:
            bo += 1
        if bo == 2: 
            return True
    return False
