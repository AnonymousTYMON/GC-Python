
print("M + (M+1) + (M+2) + ... + N")
m = int(input("M:"))
n = int(input("N:"))
output = int(0)
for i in range(m  ,n + 1):
    output += int(i)
print(str(output))
