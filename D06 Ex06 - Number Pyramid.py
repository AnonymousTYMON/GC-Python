num = int(input("Input a number:"))
for x in range(1, (num + 1)):
    for y in range(1, (int(x) + 1)):
        print(str(y), end=" ")
    print("")