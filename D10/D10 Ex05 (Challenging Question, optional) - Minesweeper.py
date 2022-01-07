import random
def checkbomb(r,c):
    if r == bomb[0] and c == bomb[1]:
        print("The bomb is here")
    if r != bomb[0] or c != bomb[1]:
        print("The bomb is not here")
minefield = []
for i in range(10):
    minefield.append([0,0,0,0,0,0,0,0,0,0])
bomb = [1,2]
bomb[0] = random.randint(1,10)
bomb[1] = random.randint(1,10)
print(bomb)
print("Guess the location of the bomb")
r = int(input())
c = int(input())
checkbomb(r,c)
