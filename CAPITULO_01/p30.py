"""P-1.30 Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2."""


#tomo el numero de cifras menos 1 en su representación binaria y eso me dice la potencia mas grande de dos al cual pertenece
def divide_by_two(n = int):
    return len(str(bin(n)[2:]))-1

print(divide_by_two(5))