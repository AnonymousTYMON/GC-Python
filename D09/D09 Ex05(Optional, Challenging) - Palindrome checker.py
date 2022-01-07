input = str(input("Input a word: "))
palindrome = ["civic","level","racecar","refer","rotor"]
is_palindrome = False
for word in palindrome:
    if input or input.lower in word:
        is_palindrome = True
if is_palindrome == True:
    print(input + " is a palindrome.")
else:
    print(input + " is not a palindrome")