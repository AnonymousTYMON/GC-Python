import random
select_team = True
hero1 = str(input("Input name of hero #1:  "))
hero2 = str(input("Input name of hero #2:  "))
hero3 = str(input("Input name of hero #3:  "))
hero4 = str(input("Input name of hero #4:  "))
hero5 = str(input("Input name of hero #5:  "))
while select_team == True:
    class profile:
        def SWM(self):
            print("Type:    Swordsman, HP:  "+str(random.randint(500,700))+", ATK:  "+str(random.randint(80,255))+", DEF:  "+str(random.randint(10,255))+", SPD:  "+str(random.randint(10,255))+", MP:  "+str(random.randint(10,30)))
        def ASN(self):
            print("Type:    Assassin, HP:  " + str(random.randint(300,500)) + ", ATK:  " + str(random.randint(10,255)) + ", DEF:  " + str(random.randint(10,255)) + ", SPD:  " + str(random.randint(10,255)) + ", MP:  " + str(random.randint(10,30)))
        def THF(self):
            print("Type:    Thief, HP:  " + str(random.randint(300,500)) + ", ATK:  " + str(random.randint(10,255)) + ", DEF:  " + str(random.randint(10,255)) + ", SPD:  " + str(random.randint(100,255)) + ", MP:  " + str(random.randint(10,50)))
        def PST(self):
            print("Type:    Priest, HP:  " + str(random.randint(100,1000)) + ", ATK:  " + str(random.randint(10,255)) + ", DEF:  " + str(random.randint(10,255)) + ", SPD:  " + str(random.randint(10,255)) + ", MP:  " + str(random.randint(10,50)))
        def FIY(self):
            print("Type:    Fairy, HP:  " + str(random.randint(100,1000)) + ", ATK:  " + str(random.randint(10,255)) + ", DEF:  " + str(random.randint(10,255)) + ", SPD:  " + str(random.randint(10,255)) + ", MP:  " + str(random.randint(10,50)))
    hero = profile()
    print("Hero 1: "+ hero1)
    random.choice((hero.SWM,hero.ASN,hero.THF,hero.PST,hero.FIY))()
    print("Hero 2: "+ hero2)
    random.choice((hero.SWM,hero.ASN,hero.THF,hero.PST,hero.FIY))()
    print("Hero 3: "+ hero3)
    random.choice((hero.SWM,hero.ASN,hero.THF,hero.PST,hero.FIY))()
    print("Hero 4: "+ hero4)
    random.choice((hero.SWM,hero.ASN,hero.THF,hero.PST,hero.FIY))()
    print("Hero 5: "+ hero5)
    random.choice((hero.SWM,hero.ASN,hero.THF,hero.PST,hero.FIY))()
    print("Use this team?   (Y/N)")
    YN = str(input())
    if YN == "Y":
        select_team = False
    elif YN != "N" or YN != "Y":
        valid = False
        while valid == False:
            print("Please input Y or N")
            YN = str(input())
            if YN == "Y" or YN == "N":
                valid = True
print("Your team is done!")
