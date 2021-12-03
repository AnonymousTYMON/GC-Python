def dailywage(hours):
    if hours > 8:
        return (hours * 37.5) + (hours - 8) * 5
    elif hours > 12:
        print("You should work for more than 12 hours a day")
    else:
        return hours * 37.5
hours = input("Please enter the number of hours worked:")
money = dailywage(int(hours))
print("The wage for today is: "+ str(money))