"""C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.

Usamos la función chr(integer)
Vemos que en unicode los caracteres del alfabeto inglés van del 65 al 90,
entonces lo uqe tenemos que hacer es un ciclo desde 65 hasta 91, aplicando
la funcion chr(i).

vemos:
"""
a = [ chr(i) for i in range(65,91)]
