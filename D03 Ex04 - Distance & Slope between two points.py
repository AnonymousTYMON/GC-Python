import math
print("Give two point")
x1 = input("x-coordinate of pt1:")
y1 = input("y-coordinate of pt1:")
x2 = input("x-coordinate of pt2:")
y2 = input("y-coordinate of pt2:")
d = math.sqrt(((float(x1)-float(x2))**2+(float(y1)-float(y2))**2))
m = (float(y2) - float(y1))/(float(x2) - float(x1))
print("The distance is "+str(d))
print("The slope is "+ str(m))