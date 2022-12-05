#OPERADORES

"""
+	Realiza Adición entre los operandos	                12 + 3 = 15
-	Realiza Substracción entre los operandos	        12 - 3 = 9
*	Realiza Multiplicación entre los operandos	        12 * 3 = 36
/	Realiza División entre los operandos	            12 / 3 = 4
%	Realiza un módulo entre los operandos	            16 % 3 = 1
**	Realiza la potencia de los operandos	            12 ** 3 = 1728
//	Realiza la división con resultado de número entero	18 // 5 = 3
"""

print(12 + 3)
print(12 - 3)
print(12 * 3)
print(12 / 3)
print(12 % 3)
print(12 ** 3)
print(12 // 3)

#Algunos símbolos como el "+" nos ayuda a concatenar por ejemplo cadenas, pero no podremos concatenar variables de diferente tipo
#Para concatenar un string y un número por ejemplo.... habría que utilizar una función del sistema como str:

print("Hola a todos " + "y a todas.")

#Lo que si podemos hacer es tipar las variables con funciones del sistema para poder concatenar difere tes tipos de variables
print("Soy el número " + str(5))

#Algo útil que podemos hacer con números es algo como
print(5 + 3 * 5 // 2 ** 3)

#Sin embargo algo que si permite python es
print("Hola " * 3)

#Operadores comparativos
"""
    1.- > mayor que
    2.- < menor que
    3.- >= mayor o igual que
    4. <= menor o igual que
    5. = igual que
    6. != distinto de
"""

print("*************** OPERADORES COMPARATIVOS ****************")
print("*************** COMPARANDO NUMEROS ****************")
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

#Para la comparación entre cadenas se realiza mediante ordenación alfabética
print("*************** OPERADORES COMPARATIVOS ****************")
print("*************** COMPARANDO CADENAS ****************")
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

#Operadores Lógicos
print("******************* OPERADORES LÓGICOS *********************")
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(not(3 > 4))

#CABE RECORDAR QUE HAY QUE APRENDERSE O SABER MUY BIEN LA LÓGICA BOOLEANA