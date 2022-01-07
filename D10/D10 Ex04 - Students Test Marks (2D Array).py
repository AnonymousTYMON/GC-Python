import random
tm = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
for i in range(0,5):
    tm[0][i] = (random.randint(0, 99))
    tm[1][i] = (random.randint(0, 99))
    tm[2][i] = (random.randint(0, 99))
    tm[3][i] = (random.randint(0, 99))
    tm[4][i] = (random.randint(0, 99))
for i2 in range(0,5):
    print("Test marks for student"+ str(i2 + 1) +": " + str(tm[i2]))
print("Student Average")
for i5 in range(0,5):
    print(str(i5+1) + "    " + str(sum(tm[i5]) / 5))
print("Test Average")
for i4 in range (0,5):
    avg = 0
    max = 0
    for i3 in range(0,5):
        avg += tm[i3][i4]
        if tm [i3][i4] > max:
            max = tm [i3][i4]
    if max == tm[0][i4]:
        print("Test" + str(i4+1) +": " + str(avg/5)+ ", " "Best student: studnet 1")
    if max == tm[1][i4]:
        print("Test" + str(i4+1) +": " + str(avg/5)+ ", " "Best student: studnet 2")
    if max == tm[2][i4]:
        print("Test" + str(i4+1) +": " + str(avg/5)+ ", " "Best student: studnet 3")
    if max == tm[3][i4]:
        print("Test" + str(i4+1) +": " + str(avg/5)+ ", " "Best student: studnet 4")
    if max == tm[4][i4]:
        print("Test" + str(i4+1) +": " + str(avg/5)+ ", " "Best student: studnet 5")
