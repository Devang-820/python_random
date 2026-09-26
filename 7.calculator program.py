OPERATOR = input("Enter the operator (+ - * /): ")


num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if OPERATOR == "+":
        result = num1 + num2
        print(round(result, 3))

elif OPERATOR == "-":
        result = num1 - num2
        print(round(result, 3))

elif OPERATOR == "*":
        result = num1 * num2
        print(round(result, 3))

elif OPERATOR == "/":
        result = num1 / num2
        print(round(result, 3))

else:
        print(f"{OPERATOR} is not a valid operator")


   
