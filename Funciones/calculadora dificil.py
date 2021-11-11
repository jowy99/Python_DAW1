def detector_suma(string, posicion):
    num1 = string[0:posicion]
    num2 = string[posicion + 1:]
    if num1.isdigit():
        if num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            return num1 + num2

def detector_resta(string, posicion):
    num1 = string[0:posicion]
    num2 = string[posicion + 1:]
    if num1.isdigit():
        if num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            return num1 - num2

def detector_multiplicacion(string, posicion):
    num1 = string[0:posicion]
    num2 = string[posicion + 1:]
    if num1.isdigit():
        if num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            return num1 * num2

def detector_division(string, posicion):
    num1 = string[0:posicion]
    num2 = string[posicion + 1:]
    if num1.isdigit():
        if num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            return num1 / num2


while True:
    calculadora = input("¿Qué quieres hace? ")
    calculadora.lower()

    if "+" in calculadora:

        posicion = calculadora.find("+")

        print(detector_suma(calculadora, posicion))

    elif "-" in calculadora:

        posicion = calculadora.find("-")

        print(detector_resta(calculadora, posicion))

    elif "*" in calculadora:

        posicion = calculadora.find("*")

        print(detector_multiplicacion(calculadora, posicion))

    elif "/" in calculadora:

        posicion = calculadora.find("/")

        print(detector_division(calculadora, posicion))

    elif calculadora == "salir":
        break