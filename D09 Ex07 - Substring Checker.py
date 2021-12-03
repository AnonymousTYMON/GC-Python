str1 = str(input("Input string 1:"))
str2 = str(input("Input string 2:"))
if str2 in str1:
    print(str2 +" is a substring of "+ str1)
else: print(str1 +" is not a substring of "+ str2)