stick = int(7)
print("Stick Picking Game\nWhoever picks up the last stick loses\nEach player takes turns picking up 1, 2 or 3 sticks and no pass is allowed.")
p1 = int(0)
p2 = int(0)
pick_no = int(0)
loser = True
game = True
while game == True:
    p1_turn = True
    p2_turn = True
    while p1_turn == True and game == True:
        print("The number of sticks on the table: " + str(stick))
        pick_no = int(input("Player 1's turn:"))
        if pick_no <= 3 and pick_no >= 1 and pick_no <= stick:
            stick -= pick_no
            p1_turn = False
        else:
            print("You can only pick up 1, 2 or 3 sticks, plz try again")
        if stick == int(1):
            game = False
            loser = False
        if stick == int(0):
            game = False
            loser = True
    while p2_turn == True and game == True:
        print("The number of sticks on the table: " + str(stick))
        pick_no = int(input("Player 2's turn:"))
        if pick_no <= 3 and pick_no >= 1 and pick_no <= stick:
            stick -= pick_no
            p2_turn = False
        else:
            print("You can only pick up 1, 2 or 3 sticks, plz try again")
        if stick == int(1):
            game = False
            loser = True
        if stick == int(0):
            game = False
            loser = False
if loser == True:
    print("Player2 won!")
else:
    print("PLayer1 won!")
