from art import logo

print(logo)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n")

at_cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

if at_cross_road == 'left':
    at_lake = input("You've come to a lake. There is an island in the middle of the lake."
                    " Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()

    if at_lake == 'wait':
        at_island = input("You arrive at the island unharmed. There is a house with 3 doors. "
                          "One red, one yellow and one blue. Which colour do you choose?\n").lower()

        if at_island == 'yellow':
            print("You found the treasure! You Win!")
        elif at_island == 'red':
            print("It's a room full of fire. Game Over.")
        elif at_island == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
