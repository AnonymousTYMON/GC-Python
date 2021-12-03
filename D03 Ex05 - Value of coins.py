def coinvalue(a, b, c):
    return (a * 0.1) + (b * 0.2) + (c * 0.5)
a = input("Number of 10c:")
b = input("Number of 20c:")
c = input("Number of 50c:")
d = coinvalue(int(a), int(b), int(c))
print("The total value of the coins is $"+ str(d))