# Define the function needed
# print options to the user
# ask for values
# call the function
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b 
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b 
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a * b 
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

while True:

    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input youre choice: ")

    if choice == "a" or choice == "A":
        input("You're choice is Addition")
        a = int(input("Input a: "))
        b = int(input("Input b: "))
        add(a, b)

    elif choice == "b" or choice == "B":
        input("You're choice is Substraction")
        a = int(input("Input a: "))
        b = int(input("Input b: "))
        sub(a, b)


    elif choice == "c" or choice == "C":
        input("You're choice is Multiplication")
        a = int(input("Input a: "))
        b = int(input("Input b: "))
        mul(a, b)


    elif choice == "d" or choice == "D":
        input("You're choice is Division")
        a = int(input("Input a: "))
        b = int(input("Input b: "))
        div(a, b)

    elif choice == "e" or choice == "E":
        print("Program ended")
        quit()



