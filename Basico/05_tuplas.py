#TUPLAS

#Definir una tupla, una tupla es un cojunto de valores o elementos
#La principal diferencia entre una lista y una tupla, es que la tupla es inmutable, es decir, no se pueden modificar sus valores
#No se pueden agregar elementos, ni borrar
my_tupla = tuple()
my_other_tupla = ()

my_tupla = (38, 1.76, "Alejandro")
my_other_tupla = (20, 25, 37, 42)

#Las funciones son similares que a las listas
#Imprimniendo la tupla
print(my_tupla)
#Imprimiendo el tipo 
print(type(my_tupla))
#Imprimiendo el valor del elemento en la posicion 1 de la tupla
print(my_tupla[1])
#Contara cuantos valores se repiten en la tupla, con los que se encuentran entre el paréntesis de la función count
print(my_tupla.count(38))
#Nos devolverá el índice en el cual se encuentra el valor definido entre paréntesis de la funcion index
print(my_tupla.index(38))
#Se pueden sumar
my_suma_tupla = my_tupla + my_other_tupla
print(my_suma_tupla)
