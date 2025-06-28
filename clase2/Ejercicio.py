#crear un programa que pida dos numeros y obtenga como resultado cual de ellos es par
#o si ambos son pares.

dato = int(input("Introduce el primer numero: "))
dato2 = int(input("Introduce el segundo numero: "))
if dato % 2 == 0 and dato2 % 2 == 0:
    print("Ambos numeros son pares")
elif dato % 2 == 0:
    print(f"El primer numero {dato} es par")
elif dato2 % 2 == 0:
    print(f"El segundo numero {dato2} es par")
else:
    print("Ninguno de los numeros es par")
# Fin del ejercicio