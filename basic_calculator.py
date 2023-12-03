# Define the function + - * /
def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

print("A, Addition")
print("B, Subtraction")
print("C, Multiplication")  # Mengganti "Multification" menjadi "Multiplication"
print("D, Division")
print("E, Exit")  # Mengganti "exit" menjadi "Exit"

choice = input("Input your choice: ")

if choice.upper() == "A":
    print("Addition")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    add(a, b)
elif choice.upper() == "B":
    print("Subtraction")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    sub(a, b)
elif choice.upper() == "C":
    print("Multiplication")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    mul(a, b)
elif choice.upper() == "D":
    print("Division")
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    div(a, b)
elif choice.upper() == "E":
    print("Quit Program")
else:
    print("Invalid Choice")
