def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

calculadora = int(input("¿Que operación quieres realizar?\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n"))

if calculadora == 1:
    n1 = float(input("Introduce un número: "))
    print("%.2f + " % n1)
    n2 = float(input("Introduce otro número: "))
    print("%.2f + %.2f = %.2f" % (n1, n2, suma(n1,n2)))
elif calculadora == 2:
    n1 = float(input("Introduce un número: "))
    print("%.2f - " % n1)
    n2 = float(input("Introduce otro número: "))
    print("%.2f - %.2f = %.2f" % (n1, n2, resta(n1,n2)))
elif calculadora == 3:
    n1 = float(input("Introduce un número: "))
    print("%.2f x " % n1)
    n2 = float(input("Introduce otro número: "))
    print("%.2f x %.2f = %.2f" % (n1, n2, multiplicacion(n1,n2)))
elif calculadora == 4:
    n1 = float(input("Introduce un número: "))
    print("%.2f / " % n1)
    n2 = float(input("Introduce otro número: "))
    print("%.2f / %.2f = %.2f" % (n1, n2, division(n1,n2)))
else:
    print("No existe esa operación.")