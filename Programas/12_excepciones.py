### Excepciones ###
### Manejo de errores ###

num1 = 5
num2 = 6
num3 = 7

try:
    print(num1 + num2)
    print("No hay errores")
except:
    print("Se ha producido un error")
else: #Es OPCIONAL
    #Se ejecuta si no se produce una excepción#
    print("La ejecución continúa sin problema")
finally: #Es OPCIONAL
    #Se ejecuta haya o no haya excepción, es decir, siempre#
    print("La ejecución continúa")

print("================================================================")
print("================================================================")

# Captura de excepciones por tipo
try:
    print(num1 + num3)
    print("No hay errores")
except TypeError:
    print("Se ha producido un error de tipo")
except ValueError:
    print("Se ha producido un error de valor")

print("================================================================")
print("================================================================")

#Captura del valor de la excepción
try:
    print(num2 + num3)
    print("No hay errores")
except TypeError:
    print("Se ha producido un error de tipo")
except ValueError:
    print("Se ha producido un error de valor")
except Exception as e: 
    print(e)