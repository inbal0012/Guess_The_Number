import random


def guess_a_num():
    guess = 0;

    while guess == 0:
        try:
            guess = int(input("Guess a number between 1 abd 20: "))
        except:
            print("Invalid input")

    return guess


number = random.randrange(1, 20)
guess = guess_a_num()
tries = 1

while guess != number:
    if guess < number:
        print("You need to guess higher. Try again")
        guess = guess_a_num()
    else:
        print("You need to guess lower. Try again")
        guess = guess_a_num()
    tries+=1

print("\nYou guessed the number correctly!\nAnd it took you " + str(tries) + " tries")
