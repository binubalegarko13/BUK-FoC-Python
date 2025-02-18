def greet(name):
    greeting = "Hello " + name
    return greeting

def enter_name():
    name = input("Enter your name: ")
    return name

def input_age():
    age = int(input("Enter your age: "))
    return age

def main():
    name = enter_name()
    greeting = greet(name)
    age = input_age()
    if age >= 18:
        print(greeting + ", you are an adult.")
    else:
        print(f"{greeting}, You are a Child")

main()



#By Usman Abdullahi (Information Technology Department)