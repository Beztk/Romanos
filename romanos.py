"""

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
"""


def convertir_a_romano(numero):
    if type(numero) != int:
        return f"Error: debes introducir un número entero ({numero})"

    # validar el valor del número
    if not (0 < numero < 4000):
        return f"Error: el número debe estar entre 1 y 3999 ({numero})"

    conversores = [
        ["", "M", "MM", "MMM"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ]

    divisores = [1000, 100, 10, 1]

    resultado = ""
    contador = 0

    for divisor in divisores:
        cociente = (numero // divisor)
        numero = numero % divisor
        resultado = resultado + conversores[contador][cociente]
        contador = contador + 1

    return resultado


def romano_a_entero(romano):

    digitos_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    romanos_repetidos = ['IIII', ' VVVV',
                         'XXXX', 'LLLL', 'CCCC', 'DDDD', 'MMMM']

    if not isinstance(romano, str):
        return 'ERROR: tiene que ser un número romano en formato cadena de texto'

    resultado = 0
    anterior = 0

    for letra in romano:
        if letra not in digitos_romanos:
            return f'ERROR: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)'
        actual = digitos_romanos[letra]

        if valor in romanos_repetidos:
            return f'ERROR: {valor} no es permitido'

        if anterior < actual:
            # comprobar que la resta es posible
            # el orden de magnitud no es mayor de uno

            if anterior > 0 and len(str(actual)) - len(str(anterior)) > 1:
                return f"ERROR: resta no posible (ant: {anterior}, act: {actual})"

            # deshacer la suma (que hemos hecho en la iteración anterior)
            # DCI --- DC
            resultado = resultado - anterior
            # DC(IV) 600 + 4 = 600 + (5 - 1) = resultado + (actual - anterior)
            # sumar el valor actual, pero restando el anterior
            resultado = resultado + (actual - anterior)
        else:
            resultado = resultado + actual

        anterior = actual

    return resultado


"""

3 -- 56

        10³10²10¹10⁰
.  .  .  .  .  .  .
         3  0  0  0  3*10³ --- 4
            3  0  0  3*10² --- 3
               3  0  3*10¹ --- 2
                  3  3*10⁰ --- 1

midamos la longitud del número

I - 1           1*10⁰
X - 10          1*10¹

I - 1           1*10⁰
C - 100         1*10²

I   1*10⁰
V   5*10⁰

I   1*10⁰
D   5*10²


I -- 1
D -- 500
len("1") 1
len("500") 3
"""


errores = ['A', '', 3, ['X', 'X', 'I']]
pruebas = ['IIII', 'I', 'MCXXIII', 'VIII', 'LVI', 'IV',
           'IX', 'XC', 'CM', 'IC', 'IM', 'XM', 'ID', 'VX']

for valor in pruebas:
    print(romano_a_entero(valor))
# print(romano_a_entero('MCXCIV'))
