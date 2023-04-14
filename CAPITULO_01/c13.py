"""C-1.13 Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing."""
""""
tengo que la función reversed() invierte los elementos 
de una lista iterable, pero no se explica su funcionamiento
en el primer capitulo, solo dice lo que hace.

pseudocodigo :
ciclo invertido dentro de los elementos de la lista
crear nueva lista e ir añadiendo las iteraciones de la lista.
retornar lista invertida


La diferencia es que el metodo de python invierte la lista en si misma
y mi funcion lo que hace es crear una nueva lista
para ir añadiendo los elementos ahi y luego retornar esa lista, 
mi funcion no modifica la lista, sino que retorna una nueva, pero
reversed() si invierte la lista en si.
"""