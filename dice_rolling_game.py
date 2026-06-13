import random

while True:
    choice = input("Roll the dice? (yes/no): ").lower()

    if choice == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1}, {dice2})")

    elif choice == "no":
        print("Thank you for playing the game!")
        break

    else:
        print("Invalid input!")
   

