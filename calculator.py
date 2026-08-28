# Taking numeric inputs from the user and converting them to decimal numbers
num1 = float(input("Enter first:"))
num2 = float(input("Enter second:"))

# Taking the operation choice from the user
choice = input("Enter(1/2/3/4:")

# Condition for Addition
if choice=='1':
    print(num1+num2)

# Condition for Subtraction
elif choice=='2':
    print(num1-num2)

# Condition for Multiplication
elif choice=='3':
    print(num1*num2)

# Condition for Division with safety check
elif choice=='4':
    # Checking if the denominator is not zero to prevent runtime crashes
    if num2!=0:
        print(num1/num2)
    else:
        print("zero error")

# Handling invalid choice inputs
else :
    print("invalid")
