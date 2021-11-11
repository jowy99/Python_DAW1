def vocal(letra):
    
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return True
    elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        return True
    else:
        return False

print("Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.")

letra = input("Escribe una letra: ")

sol = vocal(letra)

print(sol)