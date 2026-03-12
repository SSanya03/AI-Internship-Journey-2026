#prgrm4: Simple Calculator
num1 = int(input("Enter 1st integer:"))
num2 = int(input("Enter 2nd integer:"))
operation = input("Choose operator('+','-','*','/'):")
if operation == '+':
    print(f"Result: {num1+num2}")
elif operation == '-':
    print(f"Result: {num1-num2}")
elif operation == '*':
    print(f"Result: {num1*num2}")
elif operation == '/':
    print(f"Result: {num1/num2}")
else:
    print("Invalid")