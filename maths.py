print("Do you want to Add,Subtract, Multiply,Divide")
print("1:Add")
print("2 Subtraction")
print("3: Multiplication")
print("4: Divison")

option = int(input("Enter an option: "))

if option == 1:
    x = int(input("Enter first number:  "))

    y = int(input("Enter Second number: "))
    
    result = x + y
    
    print(result)
    
if option == 2:
    x = int(input("Enter first number:  "))

    y = int(input("Enter Second number: "))
    
    result = x - y
    
    print(result)

if option == 3:
    x = int(input("Enter first number:  "))

    y = int(input("Enter Second number: "))
    
    result = x * y
    
    print(result)


if option == 4:
    x = int(input("Enter first number:  "))

    y = int(input("Enter Second number: "))
    
    result = x / y
    
    print(result)
    
else:
    print("you didnt select any of the options ")

