principal = int(input("Principal?"))
rate = int(input("Interest Rate?"))
year = int(input("Number of years?"))
amount = int(0)
print("\n\nYear   Amount")
for each_year in range(1, (year + 1)):
    amount = int(principal * (1 + rate/100)**int(each_year))
    print(str(each_year)+"      "+ str(amount))