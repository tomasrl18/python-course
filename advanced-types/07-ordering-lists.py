numbers = [2, 4, 1, 45, 75, 22]

#numbers.sort()
#numbers.sort(reverse=True)
numbers2 = sorted(numbers, reverse=True)
print(numbers)
print(numbers2)

users = [[4, "Chachito"], [1, "Felipe"], [5, "Pulga"]]
users2 = [["Chachito", 4], ["Felipe", 1], ["Pulga", 5]]
users.sort()
users2.sort()
print(users)
print(users2)


users2.sort(key=lambda el: el[1])
print(users2)