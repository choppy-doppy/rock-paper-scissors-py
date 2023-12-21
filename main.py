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


def computer_turn():
    options = ("rock", "paper", "scissors")

    computer_play = random.choice(options)

    return computer_play


def main():
    user_play = input_gather()
    computer_play = computer_turn()
    while True:
        if user_play == "rock":
            if computer_play == "paper":
                print(computer_play)
                print("i win")
                break
            elif computer_play == "scissors":
                print(computer_play)
                print("i lose :(")
                break
            else:
                print(computer_play)
                print("draw")
                break

        if user_play == "paper":
            if computer_play == "scissors":
                print(computer_play)
                print("i win")
                break
            elif computer_play == "rock":
                print(computer_play)
                print("i lose :(")
                break
            else:
                print(computer_play)
                print("draw")
                break

        if user_play == "scissors":
            if computer_play == "rock":
                print(computer_play)
                print("i win")
                break
            elif computer_play == "paper":
                print(computer_play)
                print("i lose :(")
                break
            else:
                print(computer_play)
                print("draw")
                break

    main()


main()
