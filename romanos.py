def convertir_a_romano(numero):
    if type(numero) != int:
        return f"Error: debes introducir un numero entero ({numero})"
    elif type(numero) == int:
        return "TODO: convertir a romano"


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
