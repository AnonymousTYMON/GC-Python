#Hamming Distance
print("Input two strings which have the same length:")
str1 = str(input(""))
str2 = str(input(""))
if len(str1) < len(str2):
    cache = str1
    str1 = str2
    str2 = cache
len1 = len(str1)
len2 = len(str2)
len_difference = len1 - len2
max = int(0)
for i2 in range(0, len_difference+1):
    HM = int(0)
    for i in range(0,len2):
        if str1[i+i2] == str2[i]:
            HM += 1
    if max < HM:
        max = HM
dissimilar = int(len1 - max)
per_dissimilar = int((dissimilar/int(len1)) * 100)
print(str(per_dissimilar) +"% of these two characters are not similar")
