valid = True
while valid == True:
    condition = int(0)
    length = False
    lower = False
    upper = False
    digit = False
    symbol = False
    password = str(input("Input your password:"))
    if len(password) > 10:
        length = True
    for letter in password:
        if letter.islower():
            lower = True
        if letter.isupper():
            upper = True
        if letter.isdigit():
            digit = True
        if "!" or "@" or "#" or "$" or "%" or "^" or "&" or "*" or "(" or ")" or "-" or "_" or "+" or "=" or "?" or "," or "." or "<" or ">" in letter:
            symbol = True
    if length == True:
        condition += 1
    if lower == True:
        condition += 1
    if upper == True:
        condition += 1
    if digit == True:
        condition += 1
    if symbol == True:
        condition += 1
    if condition == 5:
        valid = False
    else:
        print("Your password is not validatable, please try again")
print("Your password is validate\n Repeat your password: "+ str(password))
