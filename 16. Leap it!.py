leap_year = []
for i in range (1,9999):
    if (i % 4) == 0:
        leap_year.append(i)
random_year = int(input("Input a year\n"))
is_leap = False
for i2 in leap_year:
    if random_year == i2:
        is_leap = True
if is_leap == False:
    print("It is not a leap year")
if is_leap == True:
    print("It is a leap year")
