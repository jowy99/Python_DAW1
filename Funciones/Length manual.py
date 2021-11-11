def length_manual(cadena):
    contador = 0

    for i in cadena:
        contador += 1
    return contador

print("Definir una función que calcule la longitud de una lista o una cadena dada.")

cadena = list(input("Escribe una cadena: "))

sol = length_manual(cadena)

print(sol)