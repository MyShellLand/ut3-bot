import copy
import logging

logging.basicConfig(level=logging.DEBUG)

g = ['x','-','-','-','o','-','o','-','x']


def best_move(g,player):

    moves = []
    scores = []
    other = 'x' if player == 'o' else 'o'

    for move in children(g,player):
        moves.append(move)
        scores.append(solve(move,other))

    if player == 'x':
        best = -1
        for i, score in enumerate(scores):
            if score > best:
                best = score
                bestIndex = i

    elif player == 'x':
        best = 1
        for i, score in enumerate(scores):
            if score < best:
                best = score
                bestIndex = i

    board_after_best_move = moves[bestIndex]
    evaluation = scores[bestIndex]

    logging.debug(moves)
    logging.debug(scores)
    logging.debug(bestIndex)

    print(evaluation)
    return board_after_best_move





def solve(g,player):  # should spit out -1 to 1 for evaluation
    logging.debug(f'trying to solve {g}')
    result = won(g)
    if result:
        return result

    if player == 'x':
        maxEval = -1
        for child in children(g,player):
            eval = solve(child,'o')
            maxEval = max(maxEval,eval)
        return maxEval

    else:
        minEval = 1
        for child in children(g,player):
            eval = solve(child,'x')
            minEval = min(minEval,eval)
        return minEval


def won(g):
    if g[0]==g[1]==g[2]=='x'or g[3]==g[4]==g[5]=='x'or g[6]==g[7]==g[8]=='x'or g[0]==g[3]==g[6]=='x'or g[1]==g[4]==g[7]=='x'or g[2]==g[5]==g[8]=='x'or g[0]==g[4]==g[8]=='x'or g[2]==g[4]==g[8]=='x':
        logging.debug(f'x wins in board {g}')
        return 1
    elif g[0]==g[1]==g[2]=='o'or g[3]==g[4]==g[5]=='o'or g[6]==g[7]==g[8]=='o'or g[0]==g[3]==g[6]=='o'or g[1]==g[4]==g[7]=='o'or g[2]==g[5]==g[8]=='o'or g[0]==g[4]==g[8]=='o'or g[2]==g[4]==g[8]=='o':
        logging.debug(f'o wins in board {g}')
        return -1
    elif g.count('-') == 0:
        logging.debug(f'draw in board {g}')
        return -.01


def children(g,player):
    branches = []
    for square in range(9):
        if g[square] == '-':
            branches.append(copy.deepcopy(g))
            branches[-1][square] = player
    logging.debug(f'the board has {len(branches)} children')
    return branches


print(best_move(g,'x'))