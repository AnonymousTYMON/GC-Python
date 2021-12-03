string1 = len(str(input("Input string 1:")))
string2 = len(str(input("Input string 2:")))
print("Length of string 1: "+ str(string1))
print("Length of string 2: "+ str(string2))
if int(string1) > int(string2):
    print("String 1 is a longer string.")
if int(string1) < int(string2):
    print("String 2 is a longer string.")
if int(string1) == int(string2):
    print("Both length of string are the same!")
