input = str(input("Input a string: "))
len_in = len(input)
length = True
for a in range(0, len_in):
    print(input[a], end=" ")
print()
for m in range(2, len_in):
    length = True
    while length == True:
        for i in range(0, len_in):
            output =str(input[i:i+m])
            if len(output) == m:
                print(output, end=" ")
            if len(output) != m:
                length = False
        print()
print(input)
