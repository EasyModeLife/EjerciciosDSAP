"""P-1.31 Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible."""

dinero = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5]


def cambio(n=int):
    cambio = []
    for i in dinero:
        times = 1
        while True:
            if n - times*i >= 0:
                times += 1
            else:
                cambio.append(times-1)
                n -= i*(times-1)
                break
    return cambio

a = cambio(1204230)
for i in range(len(a)):
    if a[i] != 0:
        print(f"{a[i]} de {dinero[i]}")