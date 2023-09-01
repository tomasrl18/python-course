greeting = "Hello global"

def greet():
    global greeting
    greeting = "Hello world!"
    print(greeting)

def greetChanchito():
    greeting = "Hello Chanchito"
    print(greeting)

greet()
greetChanchito()