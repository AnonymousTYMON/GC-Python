import math
print("Enter the coefficients(A, B, C):")
a = input()
b = input()
c = input()
d = float(b)**2 - 4 * float(a) * float(c)
if (float(a) != 0 ) and (float(d) >= 0):
    sqrt_d = math.sqrt(float(d))
    x = ((-(float(b))) + float(sqrt_d))/(2 * float(a))
    y = ((-(float(b))) - float(sqrt_d))/(2 * float(a))
    if (float(d) == 0):
        print("Double roots. x = "+ str(x))
    else: print("Two real roots. x = "+ str(x) +", "+ str(y))
elif (float(a) == 0 ):
    print("This is not a quadratic equation.")
else: print("No real roots.")