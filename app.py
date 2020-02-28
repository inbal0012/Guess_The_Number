import random


def guess_a_num():
    guess = 0

    while guess == 0:
        try:
            guess = int(input("Guess a number between 1 abd 20: "))
        except:
            print("Invalid input")

    return guess


def show_score_board():
    f = open('Leaderboard.txt', 'r')
    leaderboard = [line.replace('\n', '') for line in f.readlines()]
    

    print("leaderboard: ")
    for i in leaderboard:
        print(i)
    f.close()


def make_leaderboard():
    f = open('Leaderboard.txt', 'w')
    f.write("1. User1, Points\n2. User2, Points\n3. User3, Points\n4. User4, Points\n5. User5, Points")


# ______________'main' start here________________ #
make_leaderboard()
show_score_board()

keep_playing = "Y"

while keep_playing.upper() == "Y":
    number = random.randrange(1, 20)
    guess = guess_a_num()
    tries = 1

    while guess != number:
        if guess < number:
            print("You need to guess higher. Try again\n")
            guess = guess_a_num()
        else:
            print("You need to guess lower. Try again\n")
            guess = guess_a_num()
        tries += 1

    print("\nYou guessed the number correctly!\nAnd it took you " + str(tries) + " tries")

    keep_playing = input("\nDo you want to keep playing? Y/N ")

show_score_board()
