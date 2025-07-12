#ejemplo de for en python


contador = 10    
for i in range(0, contador):
    print(i)  # Imprimir el valor de i en cada iteración    
    print("Fin del bucle for")  # Mensaje al finalizar el bucle

# ejemplo de for con una lista
array = [1,"futbol","pc", 2, 3, 4, 5]
array.append("nuevo elemento")  # Agregar un nuevo elemento a la lista
array.insert(2, "insertado")  # Insertar un elemento en la posición 2
array.extend([6, 7, 8])  # Agregar varios elementos al final
array.remove(3)  # Eliminar el elemento 3 de la lista
for i in range(len(array)):
    print(array[i])  # Imprimir cada elemento de la lista
    print("Fin del bucle for con lista")  # Mensaje al finalizar el bucle
