#Sets

#Un set no es una estructura ordenada, a la hora de almacenar los datos ya agreguemos nuevos datos o creemos un set,
#es desordenada, un set no admite elementos repetidos

my_set = set()
my_other_set = {}

#observamos que tipo de variables son cada una de nuestras variables
print("***** TIPO DE VARIABLES *****")
print(type(my_set))
print(type(my_other_set))

#introducimos datos en my_other_set a ver que pasa
my_other_set = {"Alejandro", "Gómez-lobo", 37}

#imprimnimos que ha pasado con la variable
print("***** CAMBIO TIPO DE VARIABLE DE MY_OTHER_SET *****")
print(type(my_other_set))

#funciones
print("***** FUNCIONES *****")
print(len(my_other_set))
my_other_set.add("Madrid")
print(my_other_set)
my_other_set.add("08-Marzo-1984")
print(my_other_set)
my_other_set.add("Madrid")
print(my_other_set)

#como comprobar si un elemento existe en un set
print("***** COMPROBANDO ELEMENTOS EXISTENTES *****")
print("Alejandro" in my_other_set)
print("Alejandr" in my_other_set)

#eliminado datos
print("***** ELIMINANDO DATOS *****")
my_other_set.remove("Madrid")
print(my_other_set)
print("***** ELIMINADO TODOS LOS ELEMENTOS *****")
my_other_set.clear()
print(len(my_other_set))

#Nos cargamos el objeto my_other_set por lo que producirá un error
#del my_other_set
#print(my_other_set)

my_set = {"Alejandro", "Gómez-lobo", 37}
my_list = list(my_set)
print(my_list)

print("***** UNIENDO SET *****")
my_new_set = my_set.union(my_other_set)
print(my_new_set)

#Mostrar los valores diferentes entre un set y otro
print("***** IMPRIMIR LA DIFERENCIA ENTRE UN SET Y OTRO")
print(my_set.difference(my_other_set))