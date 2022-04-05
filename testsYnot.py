import os
import multiprocessing


def stupid(x):
    print(f'{x}: {os.getpid()}')


if __name__ == '__main__':
    poop = multiprocessing.Pool(5)
    poop.map(stupid, range(1,10))