"""C-1.17 Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
    for val in data:
    val = factor
Explain why or why not.

No, porque el cambio al valor se le está haciendo a
la iteración, no al item de la lista, la iteración 
es un identificador que apunta a los objetos de la lista,
lo que nosotros hacemos es cambiar ese apuntado a un  nuevo
objeto que es el valor del objeto de la lista multiplicado
por el factor, entonces realmente no cambiamos el apuntador de la lista
sino el apuntador de la iteración.
Lo que deberíamos de hacer es entonces cambiar que en vez
de que el iterador sea el que cambie de valor, sea el 
objeto de nuestra lista.

"""
