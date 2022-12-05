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