def ctof(num):
    return (9 * num)/5 + 32
num = input("Enter a temperature in Degree C:")
num2 = ctof(float(num))
print(num + " degree C is equal to "+ str(num2) +" degree F")