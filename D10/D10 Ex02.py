'''
sentence = str("i am tymon")
space = []
for pos,char in enumerate(sentence):
    if (char == " "):
        space.append(pos)
print(space)
print("Modified: "+ str(sentence))

s = 'python is fun'
c = 'n'
lst = []
for pos,char in enumerate(s):
    if(char == c):
        lst.append(pos)
print(lst)
'''
sentence = str("i am tymon")
space = []
words = []
for pos,char in enumerate(sentence):
    if (char == " "):
        space.append(pos)

print(space)
print(str(sentence[0].upper())+" "+ str(sentence[2].upper()+ str(sentence[3])+" "+ str(sentence[5].upper())+ str(sentence[6:10])))
print("Modified: "+ str(sentence))