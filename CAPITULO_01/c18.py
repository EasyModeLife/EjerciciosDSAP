"""C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

Buscamos una regla para generar los valores de la lista,
es fácil de ver que la regla es x^2 + x, entonces nuestra lista
constará de los elementos que sigan esa regla, tenemos que
nuestro primer elemento es generado por i = 0, entonces
ese es el inicio de nuestro ciclo, vemos que el último elemento es generado 
por i = 9, entonces ese será nuestro útimo elemeto, lo que nos 
dejas por averiguar es el salto, el cual vemos es de de 1, pues 
los elementos generados adyacentes, cumplen que la diferencia entre
sus elementos generadores es de 1.

Ahora que sabemos la regla y el rango del ciclo que necesitamos, solo necesitamos aplicar la sintaxis.
(Hay que observar que en esta lista no hay ninguna excepción a esta regla, pero de ser así la podríamos
añardir con el condicional de comphrehension syntax, por ejemplo que se salte los terminos pares
de la sucesión)
"""
a = [ i^2 + i for i in range(0,10)]
