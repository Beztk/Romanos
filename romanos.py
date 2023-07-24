def convertir_a_romano(numero):
    if type(numero) != int:
        return f"Error: debes introducir un numero entero ({numero})"

    # validar el numero
    if not (0 < numero < 4000):
        return f"Error: el numero debe estar entre 1 y 3999 ({numero})"


def comprobar_entero(numero):
    try:
        num = int(numero)
    except ValueError:
        print(f"Error: debes introducir un numero entero ({numero})")
        return ""


print(convertir_a_romano("lo que quiera"))
print(convertir_a_romano(56))
print(convertir_a_romano(56.1))
print(convertir_a_romano([]))
print(convertir_a_romano({}))
print(convertir_a_romano(0))
print(convertir_a_romano(4000))
print(convertir_a_romano(1))
print(convertir_a_romano(3999))
