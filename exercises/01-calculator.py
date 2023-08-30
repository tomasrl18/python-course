print("Bienvenido a la calculadora")
print("Para salir escribre salir")
print("Las operaciones son suma, resta, multi y div")

result = ""

while True:
    if not result:
        result = input("Ingrese un número: ")
        
        if result.lower() == "salir":
            break
        
        result = int(result)

    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break
    
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break

    n2 = int(n2)

    if op.lower() == "suma":
        result += n2
    elif op.lower() == "resta":
        result -= n2
    elif op.lower() == "div":
        result /= n2
    elif op.lower() == "multi":
        result *= n2
    else:
        print("Operación no válida")
        break
    
    print(f"El resultado es {result}")