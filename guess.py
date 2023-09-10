from random import randint

print("\nRemember! You have 10 chances to Win!!")

for x in range(1,11):
    guessNumber = int(input("\n Enter a number for guessing between 1 to 100: "))
    randomNumber = randint(1,101)

    if guessNumber == randomNumber:
        print("\nYOU WIN !! Bravo!!")
    else:
        print("\nYou have Lost")
        print("Your Random Number was: ", randomNumber)