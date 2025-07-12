


array = [1, 2, 3, 4, 5, "futbol", "pc", True, False]

print(array)

# Acceso a los elementos de la lista
print(array[0])  # Primer elemento  
print(array[5]) 

print(len(array))  # Longitud de la lista
array.append("nuevo elemento")  # Agregar un elemento al final
print(array)
array.insert(2, "insertado")  # Insertar un elemento en una posición específica
print(array)
array.extend([6, 7, 8])  # Agregar varios elementos al final
print(array)
array.remove(3)  # Eliminar un elemento específico
print(array)
array.pop()  # Eliminar el último elemento
print(array)
array.pop(2)  # Eliminar un elemento en una posición específica
print(array)
array.clear()  # Limpiar la lista
print(array)
array = [1, 2, 3, 4, 5]  # Reiniciar la lista
array2 = [6, 7, 8, 9, 10]  # Crear otra lista
array3 = array + array2  # Concatenar listas
print(array3)  # Imprimir la lista concatenada
print("futbol" in array3)  # Verificar si un elemento está en la lista
print(array3.index(6))  # Obtener el índice de un elemento
print(array3.count("Futbol"))  # Contar cuántas veces aparece un elemento
array4= [1, 2, 3, 4, 5 ]
array4.sort()  # Ordenar la lista
print(array4)
array4.reverse()  # Invertir el orden de la lista
print(array4)
