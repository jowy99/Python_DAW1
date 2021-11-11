def sum(lista):
    suma = 0

    for i in lista:
        suma += i
    return suma

def multip(lista):
    m = 1

    for x in lista:
        m *= x
    print(m)

print("Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.")

lista = list(input("Escribe una lista de números: "))

sumsol = sum(lista)
multsol = multip(lista)

print("La suma de los números de la lista es: " + sumsol)
print("La suma de los números de la lista es: " + multsol)