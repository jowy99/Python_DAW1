# Convierte un número binario a decimal comprobando que sea decimal
def decimal_a_binario(decimal):

    exp = 0
    binario = 0

    while decimal > 0:
        digito = decimal % 2
        binario = binario + digito * 10 ** exp
        exp += 1
        decimal = decimal // 2
    return binario

decimal = int(input("Escribe un número decimal: "))

sol = decimal_a_binario(decimal)

print("El número decimal (" + str(decimal) + ") en binario es " + str(sol))