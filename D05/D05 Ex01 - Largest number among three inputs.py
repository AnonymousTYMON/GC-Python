'''
print("Enter three integers:")
x = input("The first one:")
y = input("The second one:")
z = input("The thrid one:")
print(max(x,y,z))
'''
print("Enter three integers:")
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    else: return num3

num1 = input("The first one:")
num2 = input("The second one:")
num3 = input("The thrid one:")
print("The biggest number is: "+ max_num(num1, num2, num3))
