from Сlass_Field import Field

def play():
    winner = ""
    play_field = Field()
    print("Now you are playing noughts and crosses where you play for the 'X' and start first,")
    print("and your opponent is a bot that goes to a random field")
    print("Let's find out if you can beat randomness!")
    play_field.print_field()
    while True:
        play_field.move()
        winner = play_field.test_end()
        if winner != "":
            break
        play_field.move(bot=True)
        play_field.print_field()
        winner = play_field.test_end()
        if winner != "":
            break
    play_field.print_field()
    if winner == "X":
        print("You win!")
        print("--------")
    elif winner == "O":
        print("You lose!")
        print("---------")
    else:
        print("Draw")
        print("----")
