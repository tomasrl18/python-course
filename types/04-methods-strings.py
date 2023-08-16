animal = "   happy Chanchito   "
print(animal.upper()) #All in capital
print(animal.lower()) #All in lower
print(animal.capitalize()) #The first character in capital
print(animal.title()) #The first character of each word in capital
print(animal.strip()) #Remove spaces at the end and at the beginning
print(animal.lstrip()) #Remove spaces at the beginning
print(animal.rstrip()) #Remove spaces at the end
print(animal.strip().capitalize())
print(animal.find("Ch")) #Returns the index where the match begins. -1 = Not found
print(animal.replace("a", "z")) #Replaces the first argument with the second argument in the whole string
print("Chan" in animal) #Returns true or false if the string is found in the variable
print("Chan" not in animal) #Returns true or false if the string is not found in the variable