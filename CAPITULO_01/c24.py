"""C-1.24 Write a short Python function that counts the number of vowels in a given
character string."""

def count_vowels(cadena = str, list = iter):
    counter = 0
    for i in cadena:
        i = i.lower()
        if i in list:
            counter += 1
    return counter

