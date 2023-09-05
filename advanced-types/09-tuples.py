numbers = (1, 2, 3) + (4, 5, 6)
print(numbers)

coord = tuple([1, 2])
print(coord)

lessNumbers = numbers[:2]
print(lessNumbers)

first, second, *others = numbers
print(first, second, others)

for n in numbers:
    print(n)

#numbers[0] = 5

numbersList = list(numbers)
numbersList[0] = 5
print(numbersList)