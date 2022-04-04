# this isn't going to be pretty, but hopefully it knows the moves


class UT3:
    def __init__(self):
        self.b = [['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-']]
        self.s = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        self.mover = 'x'
        self.last_move = ['hello darkness', 'my old friend']  # in [sector, square] format, with 1-9 instead of 0-8/
        self.result = ''
        self.move_history = []
        self.move_number = 1

    def end_game(self):
        g = self.s
        if g[0]==g[1]==g[2]==self.mover or g[3]==g[4]==g[5]==self.mover or g[6]==g[7]==g[8]==self.mover or g[0]==g[3]==g[6]==self.mover or g[1]==g[4]==g[7]==self.mover or g[2]==g[5]==g[8]==self.mover or g[0]==g[4]==g[8]==self.mover or g[2]==g[4]==g[8]==self.mover:
            print(f'Game Over! {self.mover} won! GG')
            print(self.move_history)
            quit()
        elif g[0]!='-'and g[1]!='-'and g[2]!='-'and g[3]!='-'and g[4]!='-'and g[5]!='-'and g[6]!='-'and g[7]!='-'and g[8]!='-':
            # if board is full but no one had won
            print(f'Game Over! Everyone loses! You all suck!')
            print(self.move_history)
            quit()

    def end_sector(self):
        g = self.b[int(self.last_move[0])-1]  # g stands for the game in the updated sector
        if g[0]==g[1]==g[2]==self.mover or g[3]==g[4]==g[5]==self.mover or g[6]==g[7]==g[8]==self.mover or g[0]==g[3]==g[6]==self.mover or g[1]==g[4]==g[7]==self.mover or g[2]==g[5]==g[8]==self.mover or g[0]==g[4]==g[8]==self.mover or g[2]==g[4]==g[6]==self.mover:
            self.b[int(self.last_move[0])-1] = ['*', '*', '*', '*', self.mover, '*', '*', '*', '*']  # update display b
            self.s[int(self.last_move[0])-1] = self.mover  # update sector board for internal use
            self.end_game()
        elif g[0]!='-'and g[1]!='-'and g[2]!='-'and g[3]!='-'and g[4]!='-'and g[5]!='-'and g[6]!='-'and g[7]!='-'and g[8]!='-':
            # this is for drawn sectors
            self.b[int(self.last_move[0]) - 1] = ['*', '*', '*', '*', '*' , '*', '*', '*', '*']
            self.s[int(self.last_move[0]) - 1] = 'd'
            self.end_game()

    def print_board(self):
        print(f'{(self.b[0])[0:3]} {(self.b[1])[0:3]} {(self.b[2])[0:3]}\n{(self.b[0])[3:6]} {(self.b[1])[3:6]} {(self.b[2])[3:6]}\n{(self.b[0])[6:9]} {(self.b[1])[6:9]} {(self.b[2])[6:9]}\n\n{(self.b[3])[0:3]} {(self.b[4])[0:3]} {(self.b[5])[0:3]}\n{(self.b[3])[3:6]} {(self.b[4])[3:6]} {(self.b[5])[3:6]}\n{(self.b[3])[6:9]} {(self.b[4])[6:9]} {(self.b[5])[6:9]}\n\n{(self.b[6])[0:3]} {(self.b[7])[0:3]} {(self.b[8])[0:3]}\n{(self.b[6])[3:6]} {(self.b[7])[3:6]} {(self.b[8])[3:6]}\n{(self.b[6])[6:9]} {(self.b[7])[6:9]} {(self.b[8])[6:9]}')

    def move(self):
        move = (input(f'[{self.move_number}] {self.mover} to move: ')).split('.')
        if self.move_number == 1 or self.check_move(move) == 'valid':
            (self.b[int(move[0])-1])[int(move[1])-1] = self.mover
            self.last_move = move
            self.move_history.append(move)
            self.end_sector()
            self.last_move = move
            if self.mover == 'x':
                self.mover = 'o'
            else:
                self.mover = 'x'
            self.move_number = self.move_number + 1
            self.print_board()
        else:
            print("invalid move, why don't you try again")

    def check_move(self,move):

        if (self.b[int(move[0])-1])[int(move[1])-1] == '-':
            if int(move[0])-1 == int(self.last_move[1])-1:
                return 'valid'
            elif self.s[int(self.last_move[1])-1] != '-':  # if last move's square matched a closed sector
                return 'valid'

        # wow, this is some pretty dense code, I'm sure it won't be a problem later ;)

    # stuff under here is the minimax ai things

    def legal_moves(self):
        legal_moves = []
        if self.s[int(self.last_move[1])-1] != '-':  # find all available squares if they send you to filled one
            for sector in range(9):
                for square in range(9):
                    if (self.b[sector])[square] == '-':
                        legal_moves.append([sector + 1, square + 1])
        else:
            for square in range(9):
                if (self.b[int(self.last_move[1])-1])[square] == '-':
                    legal_moves.append([self.last_move[1], square + 1])
        return legal_moves

    def stupid_eval(self,board):
        9 + 10

        # x is +, o is -

    def minimax(self,depth,maximizingPlayer):
        # should give eval as well as best move in position
        9 + 10

ut3 = UT3()

while True:
    ut3.move()
    print(ut3.legal_moves())
