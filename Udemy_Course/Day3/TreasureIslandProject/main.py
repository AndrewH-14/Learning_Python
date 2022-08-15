print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

# Determine which direction the user would like to head
direction = input("Once ashore you see a cave to your left and a forest to your right. Would you like to go left or right?\n")

# If the user chooses left they can continue, otherwise end the program
if "left" == direction:
    print("Upon entering the cave you see two key features.")
    print("To one side you see a pond about 100 yards across")
    print("On the other side, there is an old wooden bridge spanning a pit.")
    action = input("Would you like to swim across the pond, or cross the bridge? (Enter 'swim' or 'cross')\n")

    if "cross" == action:
        print("Even with a few wooden boards breaking, you are able to cross the bridge.")
        print("You now are faced with a red, blue, and yellow door.")
        door = input("Which door would you like to enter? (Enter 'red', 'blue', or 'yellow')\n")

        if "red" == door:
            print("Fall through a trap door.\nGame Over.")
        elif "blue" == door:
            print("Boulder rolls down an incline crushing you.\nGame Over.")
        elif "yellow" == door:
            print("The room is full of treasure!\nYou Win!")
        else:
            print("Game Over.")
    else:
        print("An unknown pulls you underwater, never to be seen again.\nGame Over.")
else:
    print("A coconut falls and hits your head, knocking you unconcious.\nGame Over.")