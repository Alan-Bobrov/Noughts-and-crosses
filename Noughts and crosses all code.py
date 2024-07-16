from random import randint

class Field:
    def __init__(self, num_free_positions=9) -> None:
        field = [[0, 1, 2, 3]]
        for i in range(1, 4):
            field.append([i, " ", " ", " "])

        self.field = field
        self.num_free_positions = num_free_positions

    def print_field(self) -> None:
        print("  Play field:")
        for i in self.field:
            for j in i:
                print(j, end=" | ")
            print()
            print("---------------")

    def move(self, bot = False):
        if bot == True:
            while True:
                position_X = randint(1, 3)
                position_Y = randint(1, 3)
                if self.test_free(position_X, position_Y):
                    self.field[position_Y][position_X] = "O"
                    self.num_free_positions -= 1
                    break
        else:
            while True:
                while True:
                    position_X = input("Write coordinates of your position along the X axis: ")
                    if position_X.isdigit() and 1 <= int(position_X) <= 3:
                        break
                    else:
                        print("You have mistace in your message")
                while True:
                    position_Y = input("Write coordinates of your position along the Y axis: ")
                    if position_Y.isdigit() and 1 <= int(position_Y) <= 3:
                        position_X = int(position_X)
                        position_Y = int(position_Y)
                        break
                    else:
                        print("You have mistace in your message")
                if self.test_free(position_X, position_Y):
                    self.field[position_Y][position_X] = "X"
                    self.num_free_positions -= 1
                    break
                else:
                    print("This cell is occupied")
            print("------------------------------------------------------")
            
    def test_free(self, position_X, position_Y) -> bool:
        if self.field[position_Y][position_X] == " ":
            return True
        return False

    def test_end(self) -> str:
        field = self.field
        for i in range(1, 4):
            row = "".join(field[i][1:])
            if row == "XXX":
                return "X"
            if row == "OOO":
                return "O"
            column = "".join([field[1][i], field[2][i], field[3][i]])
            if column == "XXX":
                return "X"
            if column == "OOO":
                return "O"
        main_diagonal = "".join([field[1][1], field[2][2], field[3][3]])
        if main_diagonal == "XXX":
            return "X"
        if main_diagonal == "OOO":
            return "O"
        anothers_diagonal = "".join([field[1][3], field[2][2], field[3][1]])
        if anothers_diagonal == "XXX":
            return "X"
        if anothers_diagonal == "OOO":
            return "O"
        if self.num_free_positions == 0:
            return "draw"
        return ""

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
    
while True:
    play()
    end = input("You will be play more? (Yes or No, if you write somethihg another a will consider it as No):").lower()
    if end == "yes":
        pass
    else:
        break