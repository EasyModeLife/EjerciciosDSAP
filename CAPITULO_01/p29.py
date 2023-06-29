"""P-1.29 Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once."""


def get_permutation(alpha):
    if alpha == []:
        return [[]]
    else:
        permutations = []
        for i in range(len(alpha)):
            
            # caso para evitar casos repetidos si existen dos elementos iguales en la lista
            # puede resultar en tiempos más largos
            if i>0 and alpha[i] in alpha[0:i]:
                continue
            
            # seleccion de la lista rest sin el elemento i 
            rest = alpha[:i] + alpha[i+1:]
            
            # llamado a la exceptuando el elemento i 
            for p in get_permutation(rest):
                permutations.append([alpha[i]] + p)
                
        return permutations
    
permutaciones = get_permutation(['c', 'a', 't','d','o','g'])

# imprimir las permtuaciones como cadenas de texto y no como listas 
for per in permutaciones:
    print(''.join(per))
