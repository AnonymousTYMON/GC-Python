import random
class student:
    def __init__(self, name, result):
        self.name = name
        self.result = result
student1 = student("A", random.randint(1,99))
student2 = student("B", random.randint(1,99))
student3 = student("C", random.randint(1,99))
student4 = student("D", random.randint(1,99))
student5 = student("E", random.randint(1,99))
print("List of all student results:")
print(student1.name + ":" + str(student1.result))
print(student2.name + ":" + str(student2.result))
print(student3.name + ":" + str(student3.result))
print(student4.name + ":" + str(student4.result))
print(student5.name + ":" + str(student5.result))
print()
if student1.result >= student1.result >= student2.result and student1.result >= student3.result and student1.result >= student4.result and student1.result >= student5.result:
    print("Best: "+ student1.name + ":" + str(student1.result))
elif student2.result >= student3.result and student2.result >= student4.result and student2.result >= student5.result:
    print("Best: " + student2.name + ":" + str(student2.result))
elif student3.result >= student4.result and student3.result >= student5.result:
    print("Best: " + student3.name + ":" + str(student3.result))
elif student4.result >= student5.result:
    print("Best: " + student4.name + ":" + str(student4.result))
else:  print("Best: " + student5.name + ":" + str(student5.result))

if student1.result <= student1.result <= student2.result and student1.result <= student3.result and student1.result <= student4.result and student1.result <= student5.result:
    print("Worst: "+ student1.name + ":" + str(student1.result))
elif student2.result <= student3.result and student2.result <= student4.result and student2.result <= student5.result:
    print("Worst: " + student2.name + ":" + str(student2.result))
elif student3.result <= student4.result and student3.result <= student5.result:
    print("Worst: " + student3.name + ":" + str(student3.result))
elif student4.result <= student5.result:
    print("Worst: " + student4.name + ":" + str(student4.result))
else:  print("Worst: " + student5.name + ":" + str(student5.result))