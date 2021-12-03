string = str(input("Enter a string:"))
vowels = int(0)
for letter in string:
    if letter in "AEIOUaeiou":
        vowels += 1
print("Number of vowels in " + string + " is "+ str(vowels))