import copy
import logging
import time
logging.basicConfig(level=logging.DEBUG)

g = [['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
     ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
     ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-']]
g2 = [['o', '-', '-', 'o', '-', '-', '-', '-', 'x'], ['-', '-', 'x', '-', '-', 'o', '-', '-', 'o'], ['-', '-', 'o', '-', '-', '-', 'x', 'x', '-'],
     ['-', '-', '-', 'o', '-', 'x', '-', '-', '-'], ['x', '-', '-', 'x', '-', '-', '-', '-', '-'], ['x', 'x', '-', '-', '-', 'o', '-', '-', '-'],
     ['-', '-', 'o', '-', '-', '-', 'o', 'x', '-'], ['-', 'o', '-', '-', '-', '-', '-', 'o', '-'], ['-', '-', 'x', '-', '-', '-', 'x', '-', 'o']]
g3 = [['x', 'x', '-', '-', '-', '-', '-', '-', '-'], ['x', 'x', '-', '-', '-', '-', '-', '-', '-'], ['x', 'x', '-', '-', '-', '-', '-', '-', '-'],
     ['x', 'x', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', 'o', '-', '-', '-', '-'], ['x', 'x', '-', '-', '-', '-', '-', '-', '-'],
     ['x', 'x', '-', '-', '-', '-', '-', '-', '-'], ['x', 'x', '-', '-', '-', '-', '-', '-', '-'], ['o', 'o', 'o', '-', 'o', 'o', '-', '-', 'o']]

def display(b):
    print(f'{(b[0])[0:3]} {(b[1])[0:3]} {(b[2])[0:3]}\n{(b[0])[3:6]} {(b[1])[3:6]} {(b[2])[3:6]}\n{(b[0])[6:9]} {(b[1])[6:9]} {(b[2])[6:9]}\n\n{(b[3])[0:3]} {(b[4])[0:3]} {(b[5])[0:3]}\n{(b[3])[3:6]} {(b[4])[3:6]} {(b[5])[3:6]}\n{(b[3])[6:9]} {(b[4])[6:9]} {(b[5])[6:9]}\n\n{(b[6])[0:3]} {(b[7])[0:3]} {(b[8])[0:3]}\n{(b[6])[3:6]} {(b[7])[3:6]} {(b[8])[3:6]}\n{(b[6])[6:9]} {(b[7])[6:9]} {(b[8])[6:9]}')


def won(g):
    n = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    for i, s in enumerate(g):
        if s[0] == s[1] == s[2] == 'x' or s[3] == s[4] == s[5] == 'x' or s[6] == s[7] == s[8] == 'x' or s[
            0] == s[3] == s[6] == 'x' or s[1] == s[4] == s[7] == 'x' or s[2] == s[5] == s[8] == 'x' or s[
            0] == s[4] == s[8] == 'x' or s[2] == s[4] == s[8] == 'x':
            n[i] = 'x'
        if s[0] == s[1] == s[2] == 'o' or s[3] == s[4] == s[5] == 'o' or s[6] == s[7] == s[8] == 'o' or s[
            0] == s[3] == s[6] == 'o' or s[1] == s[4] == s[7] == 'o' or s[2] == s[5] == s[8] == 'o' or s[
            0] == s[4] == s[8] == 'o' or s[2] == s[4] == s[8] == 'o':
            n[i] = 'y'

    if n[0] == n[1] == n[2] == 'x' or n[3] == n[4] == n[5] == 'x' or n[6] == n[7] == n[8] == 'x' or n[
        0] == n[3] == n[6] == 'x' or n[1] == n[4] == n[7] == 'x' or n[2] == n[5] == n[8] == 'x' or n[
        0] == n[4] == n[8] == 'x' or n[2] == n[4] == n[8] == 'x':
        return 100
    elif n[0] == n[1] == n[2] == 'o' or n[3] == n[4] == n[5] == 'o' or n[6] == n[7] == n[8] == 'o' or n[
        0] == n[3] == n[6] == 'o' or n[1] == n[4] == n[7] == 'o' or n[2] == n[5] == n[8] == 'o' or n[
        0] == n[4] == n[8] == 'o' or n[2] == n[4] == n[8] == 'o':
        return -100
    elif n[0] != '-' and n[1] != '-' and n[2] != '-' and n[3] != '-' and n[4] != '-' and n[5] != '-' and n[6] != '-' and \
            n[7] != '-' and n[8] != '-':
        return -.01  # I don't know why you can't just put 0 but if you put 0 it breaks


def static_eval(g):

    chrisEvalWeight = 0

    n = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    for i, s in enumerate(g):
        if s[0] == s[1] == s[2] == 'x' or s[3] == s[4] == s[5] == 'x' or s[6] == s[7] == s[8] == 'x' or s[
            0] == s[3] == s[6] == 'x' or s[1] == s[4] == s[7] == 'x' or s[2] == s[5] == s[8] == 'x' or s[
            0] == s[4] == s[8] == 'x' or s[2] == s[4] == s[8] == 'x':
            n[i] = 'x'
        if s[0] == s[1] == s[2] == 'o' or s[3] == s[4] == s[5] == 'o' or s[6] == s[7] == s[8] == 'o' or s[
            0] == s[3] == s[6] == 'o' or s[1] == s[4] == s[7] == 'o' or s[2] == s[5] == s[8] == 'o' or s[
            0] == s[4] == s[8] == 'o' or s[2] == s[4] == s[8] == 'o':
            n[i] = 'y'

    if n[0] == n[1] == n[2] == 'x' or n[3] == n[4] == n[5] == 'x' or n[6] == n[7] == n[8] == 'x' or n[
        0] == n[3] == n[6] == 'x' or n[1] == n[4] == n[7] == 'x' or n[2] == n[5] == n[8] == 'x' or n[
        0] == n[4] == n[8] == 'x' or n[2] == n[4] == n[8] == 'x':
        return 100
    elif n[0] == n[1] == n[2] == 'o' or n[3] == n[4] == n[5] == 'o' or n[6] == n[7] == n[8] == 'o' or n[
        0] == n[3] == n[6] == 'o' or n[1] == n[4] == n[7] == 'o' or n[2] == n[5] == n[8] == 'o' or n[
        0] == n[4] == n[8] == 'o' or n[2] == n[4] == n[8] == 'o':
        return -100
    elif n[0]!='-'and n[1]!='-'and n[2]!='-'and n[3]!='-'and n[4]!='-'and n[5]!='-'and n[6]!='-'and n[7]!='-'and n[8]!='-':
        return -.01  # I don't know why you can't just put 0 but if you put 0 it breaks

    else:
        evaluation = -.01
        evaluation += n.count('x')
        evaluation -= n.count('o')

        if chrisEvalWeight:
            for i, sector in enumerate(n):
                if sector == '-':
                    evaluation += g[i].count('x') * chrisEvalWeight
                    evaluation -= g[i].count('o') * chrisEvalWeight

        return evaluation


def closed_sector(s):
    if s[0] == s[1] == s[2] != '-' or s[3] == s[4] == s[5] != '-' or s[6] == s[7] == s[8] != '-' or s[
        0] == s[3] == s[6] != '-' or s[1] == s[4] == s[7] != '-' or s[2] == s[5] == s[8] != '-' or s[
        0] == s[4] == s[8] != '-' or s[2] == s[4] == s[8] != '-':
        return True
    elif s.count('-') == 0:
        return True


def children(g,sent,player):
    branches = []
    sends = []

    if closed_sector(g[sent]):
        for s, sector in enumerate(g):
            for i, square in enumerate(sector):
                if square == '-':
                    branches.append(copy.deepcopy(g))
                    branches[-1][s][i] = player
                    sends.append(i)
    else:
        for i, square in enumerate(g[sent]):
            if square == '-':
                branches.append(copy.deepcopy(g))
                branches[-1][sent][i] = player
                sends.append(i)
    return [branches,sends]


def solve(g,sent,player,depth, firstlayer=True):
    wind = won(g)
    if wind:
        return wind
    elif depth == 0:
        return static_eval(g)

    if player == 'x':
        maxEval = -100
        childs = children(g,sent,player)

        if firstlayer:
            nom = len(childs[0])

        for i, child in enumerate(childs[0]):
            eval = solve(child, childs[1][i], 'o', depth-1, firstlayer=False)
            maxEval = max(maxEval,eval)
            if firstlayer:
                print(f'{i+1} move calculated out of {nom} possible ({round((i+1)/nom*100)}%)')
        return maxEval

    if player == 'o':
        minEval = 100
        childs = children(g,sent,player)

        if firstlayer:
            nom = len(childs[0])

        for i, child in enumerate(childs[0]):
            eval = solve(child, childs[1][i], 'x', depth-1, firstlayer=False)
            minEval = min(minEval,eval)
            if firstlayer:
                print(f'{i+1} move calculated out of {nom} possible ({round((i+1)/nom*100)}%)')
        return minEval


def best_move(g,sent,player):
    pass


t = time.time()

print(solve(g3,0,'x',6))

print(f'ran for {time.time()-t} seconds')