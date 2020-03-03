import re
import random


def guess_a_num():
    # the function checks the user input
    # return a valid Integer input
    guess = 0

    while guess == 0:
        try:
            guess = int(input("Guess a number between 1 abd 20: "))
        except:
            print("Invalid input")

    return guess


def download_score_board():
    # the function take the scores from the file and parse them into an array
    # each score contain the name and the score
    # return a parsed scores array
    f = open('Leaderboard.txt', 'r')
    leaderboard = [line.replace('\n', '') for line in f.readlines()]
    scores = []
    for line in leaderboard:
        score = re.split(r'[.,]', line)
        scores.append(score)

    f.close()
    return scores


def print_leaderboard():
    # prints the leader board from the file
    scores = download_score_board()
    print("leaderboard: ")
    for i in scores:
        print(i)


def check_if_won(scores, new_score):
    # the function checks if the new score beats the current 10 highest
    # scores - an array of high scores
    # new_score - a competing new score
    # return true - if the new score beats a high score
    for idx, line in enumerate(scores):
        if int(new_score) <= int(line[1]):
            if idx < 10:
                return True


def update_leaderboard(scores):
    # the function update the leaderboard file to the new high scores
    f = open('Leaderboard.txt', 'w')
    scoresStr = ""
    for idx, line in enumerate(scores):
        if idx == 10:
            break
        scoresStr += line[0] + ", " + line[1].replace(" ", "") + "\n"
    print(scoresStr)
    f.write(scoresStr)
    f.close()


def leader(score):
    # the function manages the leader board
    # if the user reached a new high score it adds it to the leaderboard and update the file
    scores = download_score_board()
    if check_if_won(scores, score):
        username = input("Congratulations!!\nYou are on the Leader Board!\nWhat's your name? ")
        for idx, line in enumerate(scores):
            if int(score) < int(line[1]):
                print("you're on the {0} place".format(idx+1))
                new_line = [username, str('{0}').format(score)]
                scores.insert(idx, new_line)
                update_leaderboard(scores)
                break


# ______________'main' start here________________ #

keep_playing = "Y"

while keep_playing.upper() == "Y":
    number = random.randrange(1, 20)
    # number = 5
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
    leader(tries)

    keep_playing = input("\nDo you want to keep playing? Y/N ")

