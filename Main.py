import random

print("🎲 Welcome to Dice Simulator developed by Monty")

while True:
    roll = input("Press Enter to roll the Dice or type 'exit' to quit")

    if roll == "exit":
        print("Thanks for playing")
        break

    dice_number = random.randint(1,6)
    print("You Rolled:",dice_number)
