a_chr = True
while a_chr == True:
    character = str(input("Enter a character:"))
    if len(character) == 1:
        a_chr = False
    else:
        print("Only a character is acceptable")
int_chr = int(ord(character))
integer = int(input("Enter an integer:"))
if integer == 1:
    print("A character after")
else:
    print(str(integer) + " characters after " + character + " is "+ chr(int_chr + integer))
