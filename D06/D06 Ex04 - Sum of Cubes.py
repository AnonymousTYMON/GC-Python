limit = int(input("Enter the limit:"))
output = int(0)
for x in range(1, (limit + 1)):
    output += int(x)**3
print(str(output))