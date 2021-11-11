# Convierte un número binario a decimal comprobando que sea decimal

def binario_a_decimal(binario):
    
    operacion = str(binario)
    posicion = 0
    decimal = 0

    operacion = operacion[::-1]

    for i in operacion:
        digito = i
        multiplicador = 2 ** posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

binario = int(input("Escribe un número binario: "))

sol = binario_a_decimal(binario)

print("El número binario (" + str(binario) + ") en decimal es " + str(sol))