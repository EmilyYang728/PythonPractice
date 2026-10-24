firstNum = int(input("first number? "))
secondNum = int(input("second number? "))
op = str(input("enter an operator (+, -, /, *): "))

if op == "+":
    output = firstNum + secondNum
    print(output)
elif op == "-":
    output = firstNum - secondNum
    print(output)
elif op == "/":
    if secondNum == 0:
        print("no dividing by zero")
    else:
        output = firstNum / secondNum
        print(output)
elif op == "*":
    output = firstNum * secondNum
    print(output)
else:
    print("invalid operator")

