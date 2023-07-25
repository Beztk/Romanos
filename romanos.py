"""
Escribir una función en PYTHON que reciba un número entre 0 y 3999
y devuelva el número como una cadena en su representación de número romano.


I  ---> 1
V  ---> 5
X  ---> 10
L  ---> 50
C  ---> 100
D  ---> 500
M  ---> 1000

1137 ==> MCXXXVII
||||_____________ VII ---- 7 * 10⁰
|||______________ XXX ---- 3 * 10¹
||_______________ C   ---- 1 * 10²
|________________ M   ---- 1 * 10³

1M 1C 3D 7U

1137 / 1000 = 1 ----- diccionario: M
1137 % 1000 = 137

137 / 100 = 1 ------- diccionario: C
137 % 100 = 37

37 / 10 = 3 --------- diccionario: XXX
37 % 10 = 7 

7 / 1 = 7 ----------- diccionario: VII
7 % 1 = 0
"""


def convertir_a_romano(numero):
    if type(numero) != int:
        return f"Error: debes introducir un número entero ({numero})"

    # validar el valor del número
    if not (0 < numero < 4000):
        return f"Error: el número debe estar entre 1 y 3999 ({numero})"

    millares = ["", "M", "MM", "MMM"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    # valores = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
    #           (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
    #           (5, 'V'), (4, 'IV'), (1, 'I')]

    """
    1000

    2354

    2354 - 1000 = 1354 :::: M
    1354 - 1000 =  354 :::: MM
    3540 -  100 =  254 :::: MMC
    254  -  100 =  154      MMCC
    154  -  100 =   54      MMCCC
    54   -   50 =    4      MMCCCD
    4    -    4 =    0      MMCCCDIV

    como resto = 0 salgo del bucle
    """

    # descomposición en millares, decenas, centenas y unidades
    millar = numero // 1000
    centena = (numero % 1000) // 100
    decena = ((numero % 1000) % 100) // 10
    unidad = (((numero % 1000) % 100) % 10) // 1

    """
    millar = numero // 1000
    resto = numero % 1000

    centena = resto // 100
    resto = resto % 100
    
    decena = resto // 10
    resto = resto % 10
    
    unidad = resto // 1
    resto = resto % 1
    """

    # RETO: podemos simplificar el proceso en lugar de copiar/pegar las operaciones de división y módulo?

    # mapear el cociente (diccionario)
    # si hay resto, repetimos...

    romano = millares[millar] + centenas[centena] + \
        decenas[decena] + unidades[unidad]

    return romano


print(convertir_a_romano(56.1))
print(convertir_a_romano("lo que quiera"))
print(convertir_a_romano([]))
print(convertir_a_romano({}))
print(convertir_a_romano(0))
print(convertir_a_romano(4000))

print(convertir_a_romano(56))
print(convertir_a_romano(1))
print(convertir_a_romano(3999))
