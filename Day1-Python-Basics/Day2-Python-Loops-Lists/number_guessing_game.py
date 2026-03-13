#prgrm9: Number Guessing Game
import random
secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret:
    print("Correct! You guessed it.")
else:
    print(f"Wrong! The number was {secret}")