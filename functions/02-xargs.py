def suma(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)

suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)