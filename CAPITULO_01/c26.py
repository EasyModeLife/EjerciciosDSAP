"""C-1.26 Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”"""

binary_operations = {0:"+",1:"-",2:"*",3:"/",4:"**"}
def determinator(a = int, b = int, c = int):
    for i in range(len(binary_operations)):
        try:
            if eval(str(a)+binary_operations[i]+str(b)) == c:
                return str(a)+binary_operations[i]+str(b)+"="+str(c)
        except ZeroDivisionError:
            continue
    return False
def caller(a = int, b = int, c = int):
    list = [a,b,c]
    for i in list:
        temp_list = list
        temp_list.remove(i)
        for j in temp_list:
            temp_list2 = list
            temp_list2.remove(j)
            for k in temp_list2:
                if determinator(i,j,k):
                    return determinator(i,j,k)

# ## a partir de aqui puras pruebas

# safe = []
# norma = 50
# for i in range(-norma,norma,1):
#     for j in range(-norma,norma,1):
#         for k in range(-norma,norma,1):
#             c = caller(i,j,k)
#             if c:
#                 safe.append([i,j,k])


# # importing mplot3d toolkits
# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt
 
# fig = plt.figure()
 
# # syntax for 3-D projection
# ax = plt.axes(projection ='3d')
 
# # defining axes
# z = [ i[0] for i in safe]
# x = [ i[1] for i in safe]
# y = [ i[2] for i in safe]
# c = [ i+j+k for i,j,k in safe]
# ax.scatter(x, y, z, c=c)
 
# # syntax for plotting
# ax.set_title('Puntos que cumplen alguna igualdad con los operadores (+  -  *  /  ^)')

# plt.show()
