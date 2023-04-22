"""C-1.20 Python’s random module includes a function shuﬄe(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuﬄe function."""

from random import randint

def shuffle(data):
    for i in range(len(data)):
        for i in range(3):
            a = randint(0,len(data)-1)
            b = randint(0,len(data)-1)
            data[a], data[b] = data[b], data[a]
        data[i], data[i-1] = data[i-1], data[i]
    return data
