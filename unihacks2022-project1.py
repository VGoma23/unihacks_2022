# Authors: Rishi Medamanuri, Akhil Malakapalli, Naveen Ramesh, Vibhu Gomatam

print("Welcome to 'Clutch Calc!'")
print("Are you performing operations with integers or decimal numbers? (If you are using both integers and decimal numbers in this operation, please select the option for 'decimal numbers'.")
print("To stop the program, enter: 'stop'.")
option1 = input("Enter 1 for integer operations and 2 for decimal operations. \n")

i = 5
while i > 2:
    if option1 == "1":
        print("Great, you have chosen integer operations.")
        num1 = input("Enter your first integer. \n")
        operator1 = input("Enter an operator: +, -, *, / \n")
        num2 = input("Enter your second integer. \n")
        num1 = int(num1)
        num2 = int(num2)
        if operator1 == "+":
            print(f"Your calculation is: {num1} + {num2} = {num1+num2}")
        elif operator1 == "-":
            print(f"Your calculation is: {num1} - {num2} = {num1-num2}")
        elif operator1 == "*":
            print(f"Your calculation is: {num1} * {num2} = {num1*num2}")
        elif operator1 == "/":
            print(f"Your calculation is: {num1} / {num2} = {num1/num2}")
       

    if option1 == "2":
        print("Great, you have chosen decimal operations.")
        num3 = input("Enter your first decimal. \n")
        operator2 = input("Enter an operator: +, -, *, / \n")
        num4 = input("Enter your second decimal. \n")
        num3 = float(num3)
        num4 = float(num4)
        if operator2 == "+":
            print(f"Your calculation is: {num3} + {num4} = {num3+num4}")
        elif operator2 == "-":
            print(f"Your calculation is: {num3} - {num4} = {num3-num4}")
        elif operator2 == "*":
            print(f"Your calculation is: {num3} * {num4} = {num3*num4}")
        elif operator2 == "/":
            print(f"Your calculation is: {num3} / {num4} = {num3/num4}")

i = 1