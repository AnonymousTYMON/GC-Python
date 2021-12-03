n = int(input("Enter the number of simulations: \n"))
print("Simulation ended.")
a = int(0)
b = int(0)
c = int(0)
d = int(0)
e = int(0)
f = int(0)
import random
for i in range (0, n):
    m = random.randint(1, 6)
    if m == 1:
        a += 1
    if m == 2:
        b += 1
    if m == 3:
        c += 1
    if m == 4:
        d += 1
    if m == 5:
        e += 1
    if m == 6:
        f += 1
pro_a = round(int((a/n) * 100),1)
pro_b = round(int((b/n) * 100),1)
pro_c = round(int((c/n) * 100),1)
pro_d = round(int((d/n) * 100),1)
pro_e = round(int((e/n) * 100),1)
pro_f = round(int((f/n) * 100),1)
print("no. of 1s: "+ str(a) + " - "+ str(pro_a) +"%")
print("no. of 2s: "+ str(b) + " - "+ str(pro_b) +"%")
print("no. of 3s: "+ str(c) + " - "+ str(pro_c) +"%")
print("no. of 4s: "+ str(d) + " - "+ str(pro_d) +"%")
print("no. of 5s: "+ str(e) + " - "+ str(pro_e) +"%")
print("no. of 6s: "+ str(f) + " - "+ str(pro_f) +"%")