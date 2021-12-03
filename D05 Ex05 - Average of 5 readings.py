print("Please enter five readings:")
five_reading = 5
total_reading = 0
a = input("The first one\n")
if int(a) != 0:
    total_reading = int(total_reading) + int(a)
else: five_reading = int(five_reading) - 1
b = input("The second one\n")
if int(b) != 0:
    total_reading = int(total_reading) + int(b)
else: five_reading = int(five_reading) - 1
c = input("The third one\n")
if int(c) != 0:
    total_reading = int(total_reading) + int(c)
else: five_reading = int(five_reading) - 1
d = input("The fourth one\n")
if int(d) != 0:
    total_reading = int(total_reading) + int(d)
else: five_reading = int(five_reading) - 1
e = input("The fifth one\n")
if int(e) != 0:
    total_reading = int(total_reading) + int(e)
else: five_reading = int(five_reading) - 1
if int(five_reading) != 0:
    av_reading = int(total_reading) / int(five_reading)
    print("Average of " + str(five_reading) + " readings is " + str(av_reading))
else: print("No valid readings, average not calculated.")
