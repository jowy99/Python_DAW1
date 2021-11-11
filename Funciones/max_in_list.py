# Imprime el mayor número de una lista

def max_in_list(lista):
    inicio = 0
    for i in lista:
        if i > inicio:
            inicio = i
    return inicio

lista = [5, 3, 6]

print(max_in_list(lista))