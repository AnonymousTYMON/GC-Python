num = int(input("Input a number:"))
for x in range(num, 0, -1):
    for y in range(x, 0, -1):
        print(str(y), end=" ")
    print("")