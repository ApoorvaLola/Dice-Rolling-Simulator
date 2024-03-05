import random

def roll_dice(num_sides, num_rolls):
    results = []
    for _ in range(num_rolls):
        result = random.randint(1, num_sides)
        results.append(result)
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    num_sides = int(input("Enter the number of sides on the dice: "))
    num_rolls = int(input("Enter the number of rolls: "))

    if num_sides <= 0 or num_rolls <= 0:
        print("Invalid input. Please enter positive values.")
        return

    print("\nRolling the dice...\n")
    rolls = roll_dice(num_sides, num_rolls)
    for i, roll in enumerate(rolls, 1):
        print(f"Roll {i}: {roll}")

if __name__ == "__main__":
    main()

while True:
    a=input("Do you want to play again? (yes/no): ").lower()
    if a=="yes":
        main()
    elif a=="no":
        print("Thank you for playing!")
        break
    else:
        print("Invalid")
        
    
    