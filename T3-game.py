

g = ['-','-','-','-','-','-','-','-','-']


def brint():

    print(f'{g[0:3]}\n{g[3:6]}\n{g[6:9]}')


def won():
    if g[0]==g[1]==g[2]=='x'or g[3]==g[4]==g[5]=='x'or g[6]==g[7]==g[8]=='x'or g[0]==g[3]==g[6]=='x'or g[1]==g[4]==g[7]=='x'or g[2]==g[5]==g[8]=='x'or g[0]==g[4]==g[8]=='x'or g[2]==g[4]==g[8]=='x':
        return 'x wins! gg'
    elif g[0]==g[1]==g[2]=='o'or g[3]==g[4]==g[5]=='o'or g[6]==g[7]==g[8]=='o'or g[0]==g[3]==g[6]=='o'or g[1]==g[4]==g[7]=='o'or g[2]==g[5]==g[8]=='o'or g[0]==g[4]==g[8]=='o'or g[2]==g[4]==g[8]=='o':
        return 'o wins! gg'
    elif g.count('-') == 0:
        return 'draw! you both lose'


mover = 'x'

while True:
    if won():
        print(won())
        break

    move = int(input(f'player {mover} to move (1-9): ')) + -1
    if g[move] == '-':
        if mover == 'x':
            g[move] = 'x'
            brint()
            mover = 'o'
        elif mover == 'o':
            g[move] = 'o'
            brint()
            mover = 'x'
    else:
        print('invalid move')
