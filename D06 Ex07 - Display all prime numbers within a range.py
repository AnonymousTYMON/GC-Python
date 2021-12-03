print("Enter x to y")
x = int(input("x:"))
y = int(input("y:"))
for i in range(x, y+1 ):
    isPrime = True
    for j in range(2, i):
        if int(i) % int(j) == 0:
            isPrime = False
    if isPrime == True:
        print(str(i))