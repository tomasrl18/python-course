n1 = 0

if n1 == 0:
    n1 = int(input("Introduzca un número: "))
    
    while True:
        op = input("+, -, /, *: ")
        n2 = int(input("Introduzca un segundo número: "))

        if op.lower() == "salir":
            break

        if op == "+":
            n1 += n2
            print(n1)
        elif op == "-":
            n1 += n2
            print(n1)
        elif op == "/":
            n1 /= n2
            print(n1)
        elif op == "*":
            n1 *= n2
            print(n1)
