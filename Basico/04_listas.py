#LISTAS

# definir listas
#
my_list = list()
my_other_list = []

print(len(my_list))

my_other_list = [37, 21, 20, 12, 20, 10, 2, 7, 312]

print("*********** IMPRIMIENDO LA LISTA *****************")
print(my_other_list)

print("************ IMPRIMIMOS LA LONGITUD DE LA LISTA *****************")
print(len(my_other_list))

print("************ CONTANDO REPETICIONES DEL NUMERO 20 *********************")
print(my_other_list.count(20))

uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve = my_other_list

print("************ DESEMPAQUETANDO LA LISTA EN SUS UNIDADES ***********************")
print(uno)
print(dos)
print(tres)
print(cuatro)

#Se pueden sumar listas
print("********************* CONCATENANDO LISTAS ***********************")
my_aux_list = [0, 1, 2, 3, 4]
print(my_other_list + my_aux_list)


print("********************** FUNCIONES EN LAS LISTAS **************************")
#OPERANDO CON LAS LISTAS
#Agrega al final de la lista un elemento más
my_other_list.append(56)

# insertar en la posición que deseamos introduce otro valor diferente
my_other_list.insert(2, 45551)

#copiar una lista en otra
my_new_list = my_other_list.copy()

#eliminar un valor de la lista
my_other_list.remove(312)
print(my_other_list)

# Quitar el ultimo elemento de la lista y si hacemos un print de pop nos retornara el valor del elemento que ha eliminado
my_other_list.pop()
print(my_other_list.pop())
print(my_other_list)

# eliminar todos los elementos de la lista
#my_other_list.clear()

# cambiar el valor de un elemento de una lista
my_other_list[2] = 20
print(my_other_list)

print("Copia de una lista en otra antes de realizar los camnbios pertinentes")
print(my_other_list)
print(my_new_list)

#orden de listas de mayor a menor
my_other_list.sort()
my_new_list.sort()

print(my_other_list)
print(my_new_list)