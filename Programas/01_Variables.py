""" Creando variables en python
Una variable, como su propio nombre indica, es un valor almacenado en memoria el cuál puede ser modificado cuantas veces 
se quiera o se necesite. También la podemos cambiar el tipo de variable que es o va a ser, es decir: podemos tener un nombre
Según la convención de Python las variables se crearán en minúsculas, separando las letras con un _
En un print se le puede pasar cualquier tipo de variable y será capaz de transformar cada tipo de variable en una cadena
que se mostrará

"""

#Para declarar variables de tipo string podemos utilizar comillas dobles como comillas simples
my_variable = 'Hola mundo'
print(my_variable)

my_int_variable = 25
print(my_int_variable)

my_bulean = True
print(my_bulean)

#Concatenación de datos en un print en python es con ","
print(my_variable, my_int_variable, my_bulean)

#Vamos a imprimir el tupo de variable
#La función type es una función que ns dará que tipo de variable estamos manejando en ese momento
print(type(my_variable), "Hola mundo")
print(type(my_int_variable), "25")
print(type(my_bulean), "True")

#Más funciones del sistema
#Esta función cuenta los caracteres que tiene la variable incluidos los espacios 
print(len(my_variable))

#Como declarar variables en una sola línea
edad, ciudad, estado_civil, hijos = 38, "Madrid", "Casado", True 

#Ahora vamos a declarar variables a partit de un input introducido por un usuario mediante el teclado
nombre = input("¿Cuál es tu nombre?:")

print("Hola ", nombre)