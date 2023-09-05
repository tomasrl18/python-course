users = [
    ["Chachito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

#names = []
#for user in users:
#    names.append(user[0])
#print(names)

#names = [user[0] for user in users]
#print(names)

#names = [user for user in users if user[1] > 2]
#print(names)

#names = [user[0] for user in users if user[1] > 2]
#print(names)

#names = list(map(lambda user: user[0], users))
lessUsers = list(filter(lambda user: user[1] > 2, users))
print(lessUsers)