"""C-1.16 In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor. We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?"""

# porque los valores numericos son los inmutables, no la lista que introducimos
# tenemos pues que se crea un nuevo valor y la direccion
# que tiene el elemento n de la lista es cambiado tambien.