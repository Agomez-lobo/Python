## FUNCIONES

def my_function():
    print("Esto es una función")

def suma(numero1, numero2):
    valor = numero1 + numero2
    return valor

def defecto(numero1, numero2 = 5):
    print(numero1 + numero2)

my_function()
print(suma(15, 35))
defecto(10)
defecto(35,50)

