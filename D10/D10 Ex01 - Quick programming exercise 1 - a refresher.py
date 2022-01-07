import random
num = []
for i in range(0,20):
    num.append(random.randint(1,99))
averge = sum(num)/len(num)

print("The numbers are: ")
for i2 in range(0,20):
    print((num[i2]), end=" ")
print("\nNumbers in reverse order: ")
for i3 in range(19, -1, -1):
    print((num[i3]), end=" ")
print("\nThe maximum number is: "+ str(max(num)))
print("The minimum number is: "+ str(min(num)))
print("The averge value is: "+ str(round(averge, 1)))






'''
a = NUM(random.randint(1, 99))


print("The numbers are: "+ str(a.num1) + str(a.num2))
print("Numbers in reverse order: ")
print("The biggest number: ")
'''