def max(n1, n2):

    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else:
        return "Son iguales."

print("Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.")

n1 = int(input("Escribe un numero: "))
n2 = int(input("Escribe un numero: "))

sol = max(n1, n2)

print(sol)