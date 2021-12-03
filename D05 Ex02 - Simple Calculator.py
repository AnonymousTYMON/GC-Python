print("Simple Calculator")
x = input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
if int(x) <= 4:
    print("Input two numbers")
    y = input("The first one:")
    z = input("The second one:")
else:
    print("Invaild input, bye!")
if int(x) == 1:
    output = float(y) + float(z)
    print(str(y)+" + "+ str(z)+" = "+ str(output))
elif int(x) == 2:
    output = float(y) - float(z)
    print(str(y) + " - " + str(z) + " = " + str(output))
elif int(x) == 3:
    output = float(y) * float(z)
    print(str(y) + " * " + str(z) + " = " + str(output))
elif int(x) == 4:
    output = float(y) / float(z)
    print(str(y) + " + " + str(z) + " = " + str(output))