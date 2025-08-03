import random
number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    tries += 1

    if guess == number:
        print("Correct! You guessed it in", tries, "attempts.")
        break
    elif guess < number:
        print("Try higher.")
    else:
        print("Try lower.")
