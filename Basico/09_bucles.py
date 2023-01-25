### Bucles

#WHILE

my_condition = 0

while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        break

if my_condition == 10:
    print("Hemos llegado a 10")
else:
    print("Superamos el valor de 10")

print("El valor conseguido es: %d" %(my_condition))

#FOR

my_list = [35, 24, 13, 11, 20, 5, 19,75]

for elemento in my_list:
    print(elemento)
    