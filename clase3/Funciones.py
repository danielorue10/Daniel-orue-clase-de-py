#ejemplo de funciones en python


def suma(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b
resultado = suma(5, 3)
print("La suma es:", resultado)
def resta(a, b):
    """Resta dos números y devuelve el resultado."""
    return a - b
resultado = resta(10, 4)
print("La resta es:", resultado)
def multiplicacion(a, b):
    """Multiplica dos números y devuelve el resultado."""
    return a * b
resultado = multiplicacion(6, 7)
print("La multiplicación es:", resultado)
def division(a, b):
    """Divide dos números y devuelve el resultado."""
    if b == 0:
        return "Error: División por cero"
    return a / b
resultado = division(20, 5)
print("La división es:", resultado)



