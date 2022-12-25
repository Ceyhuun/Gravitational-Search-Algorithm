import random


def move(PopSize, dim, pos, vel, acc):
    for i in range(0, PopSize):
        for j in range(0, dim):
            r1 = random.random()
            vel[i, j] = r1 * vel[i, j] + acc[i, j]
            pos[i, j] = pos[i, j] + vel[i, j]

    return pos, vel
