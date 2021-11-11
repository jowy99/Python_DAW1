def max_tres(n1, n2, n3):

    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    else:
        return "Son iguales."

print("Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.")

n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro número: "))
n3 = int(input("Introduce otro número: "))

sol = max_tres(n1, n2, n3)

print(sol)