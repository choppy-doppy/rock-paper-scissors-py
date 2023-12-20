import random


def input_gather():
    while True:
        user_play = input("Rock paper scissors!\n")

        if user_play == "exit":
            quit(2)

        if user_play.isdigit():
            print("you must play rock, paper or scissors!")
        elif user_play != "rock" and user_play != "paper" and user_play != "scissors":
            print("you must play rock, paper or scissors!")
        else:
            break

    return user_play


def computer_play():
    options = ("rock", "paper", "scissors")

    opponent_play = random.choice(options)

    return opponent_play


def main():
    input_gather()

    opponent_play = computer_play()

    print(opponent_play)


while True:
    main()
