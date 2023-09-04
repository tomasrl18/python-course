numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#ugly
#first = numbers[0]
#second = numbers[1]
#third = numbers[2]

#first, second, third = numbers
#print(first, second, third)

first, second, *others, penultimate, last = numbers
print(first, second, others, penultimate, last)