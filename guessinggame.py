#guessing game
import random
print("\n Welcome to the game, try to guess the number as per the hints\n")
number = random.randrange(1,20)
guess= int(input(" Enter any number between 1 and 20: "))
while number!= guess:
        if guess < number:
                print(" Your guess was too low")
                guess = int(input("Enter number again: "))
        elif guess > number:
                print(" Your guess was too high")
                guess = int(input("Enter number again: "))
        else:
                break
print("you won")


