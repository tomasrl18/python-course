find = 10
for number in range(5):
    print(number)
    if number == find:
        print("Found", find)
        break
else:
    print("Not Found")