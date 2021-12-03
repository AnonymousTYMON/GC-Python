'''
string = str(input("Enter a string:"))
vowels = int(0)
words = int(1)
for letter in string:
    if letter in "AEIOUaeiou":
        vowels += 1
    if letter in " ":
        words += 1
print("Number of vowels in " + string + " is "+ str(vowels))
print("Number of words in the string is "+ str(words))
'''
string = str(input("Enter a string:"))
vowels = int(0)
words = len(string.split())
for letter in string:
    if letter in "AEIOUaeiou":
        vowels += 1
print("Number of vowels in " + string + " is "+ str(vowels))
print("Number of words in the string is "+ str(words))
