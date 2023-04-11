from timeit import default_timer
import math
import matplotlib.pyplot as plt
from CAPITULO_01.a04 import squaressum01
from CAPITULO_01.a05 import squaressum02

def timer(func,n):
    inicio = default_timer()
    func(n)
    fin = default_timer()
    return fin-inicio

dominio = [int(math.log(i,1.01))**2 for i in range(100) if i > 0]

imagen = [timer(squaressum01,i) for i in dominio]
imagen2 = [timer(squaressum02,i) for i in dominio]

plt.plot(dominio,imagen)
plt.plot(dominio,imagen2)
plt.ylabel('SEGUNDOS')
plt.xlabel(' n ')
plt.title(' Comparativa funciones suma de n cuadrados ')
plt.show()