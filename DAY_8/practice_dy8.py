""""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b


while True:
    print("-------Calculator--------")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulus")
    print("6.Power")

    choice = int(input("Enter choice (1-6): "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(num1, num2))

    elif choice == 2:
        print("Result:", subtract(num1, num2))

    elif choice == 3:
        print("Result:", multiply(num1, num2))

    elif choice == 4:
        print("Result:", divide(num1, num2))

    elif choice == 5:
        print("Result:", modulus(num1, num2))

    elif choice == 6:
        print("Result:", power(num1, num2))

    else:
        print("Invalid choice")

    again = input("Need again (yes/no): ")
    if again.lower() != "yes":
        print("Thank you")
        break

"""


names,gpas =[],[]
max_val=0
max_name=''

for i in range(n):
    print(f"---------student-{i+1}-------")
    name=input("enter the name: ")
    gpa=float(input("enter the cgpa: "))
        
    
    if gpa>max_val:
        max_name=name
        max_val=gpa
        
    if gpa<min_val:
        min_name=name
        min_val=gpa
        
    





























