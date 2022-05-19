num1 = float(input("Enter First Number: "))
op = input("Enter an Operator: ")
num2 = float(input("Emter the other number: "))

if op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid Operator")