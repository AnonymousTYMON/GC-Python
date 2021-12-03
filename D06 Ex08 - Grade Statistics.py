end = True
total = int(0)
credit = int(0)
Pass = int(0)
Fail = int(0)
while end == True:
    grade = str(input("Enter a grade (A-F, Z to end): "))
    if grade == str("a") or grade == str("b") or grade == str("c") or grade == str("d") or grade == str("e") or grade == str("f"):
        total += 1
        if grade == str("a") or grade == str("b") or grade == str("c") or grade == str("d") or grade == str("e"):
            Pass += 1
            if grade == str("a") or grade == str("b") or grade == str("c"):
                credit += 1
    if grade == str("f"):
        Fail += 1
    if grade == str("z"):
        end = False
credit_Per = round((credit/total) * 100, 1)
Pass_Per = round((Pass/total) * 100, 1)
Fail_Per = round((Fail/total) * 100, 1)
print("Number of credit = "+ str(credit)+ (" ("+ str(credit_Per)+ "%)"))
print("Number of pass = "+ str(Pass)+ (" ("+ str(Pass_Per)+ "%)"))
print("Number of Fail = "+ str(Fail)+ (" ("+ str(Fail_Per)+ "%)"))