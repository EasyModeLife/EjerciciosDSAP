
import matplotlib.pyplot as plt

"""P-1.29 Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once."""

from itertools import permutations

def get_permutation_differences(num):
    # Convertir el número a una cadena y generar las permutaciones
    num_str = str(num)
    perm_list = list(permutations(num_str))

    # Convertir las permutaciones a números enteros
    perm_int_list = [int(''.join(p)) for p in perm_list]

    # Calcular las diferencias y almacenarlas en una lista
    differences = [abs(p - num) for p in perm_int_list]

    return differences

number = 123456
valores = get_permutation_differences(number)



# Generar datos para la serie
# Eje x: índices de la lista (1, 2, 3, ...)
x = list(range(1, len(valores) + 1))

# Crear y mostrar la gráfica
plt.plot(x, valores, marker='o', linestyle='-', label='Sucesión')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Gráfica de la sucesión de valores')
plt.legend()
plt.grid()

plt.show()
