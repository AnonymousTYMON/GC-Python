no_ordered = input("Enter number of items orderd:")
if int(no_ordered) <= 50:
    cost = float(no_ordered) * 25
elif int(no_ordered) <= 100:
    cost = float(no_ordered) * 24.5
elif int(no_ordered) <= 200:
    cost = float(no_ordered) * 24
else:
    cost = float(no_ordered) * 23
print("Total cost is $"+ str(cost))
