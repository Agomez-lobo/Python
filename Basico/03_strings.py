### STRINGS ###

my_string = "Mi String"
my_other_string = "Mi otro String"
my_new_line_string = "Este es un string\ncon salto de linea"
my_scape_string = "\tEscapado \n escapando"

print(len(my_string))
print(len(my_other_string))

#Concatenación
print(my_string + " " + my_other_string)

#Caracteres especiales que permiten las variables de tipo string
# \n salto de linea
# \t salto de tabulación
#para evitar los caracteres especiales anteriores poniendo una contra barra "\" delante del carácter especial
print(my_new_line_string)

#FORMATEO DE STRINGS
name, surname, edad = "Alejandro", "Lobo", 38

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, edad))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, edad))
print(f"Mi nombre es {name} {surname} y mi edad es {edad}")

#Desempaquetado de caracterer
languaje = "Python"
a, b, c, d, e, f = languaje
print(a)
print(b)
print(f)

#Division de cadenas
languaje_aux = languaje[0:3]
print(languaje_aux)

#Reverse
languaje_reverse = languaje[::-1]
print(languaje_reverse)

#Métodos o funciones del sistema
# len -> nos da la longitud de la cadena
# capitalize -> pone la primera letra de la cadena en mayúcula
# upper -> todas las letras en mayusculas
# lower -> pasa todas las letras a minuscula
# isupper -> nos devolverá un boolean si todos los caracteres están en mayusculas o no
# count("x") -> cuenta cuantas letras hay iguales
# isnumeric -> nos dirá si la cadena escrita es un numero