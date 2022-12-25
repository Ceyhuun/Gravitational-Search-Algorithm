import time

import numpy

import gConstant
import gField
import massCalculation
import move
from solution import solution


def GSA(objf, lb, ub, dim, PopSize, iters):
    # GSA parameters
    ElitistCheck = 1
    Rpower = 1

    s = solution()

    """ Initializations """

    vel = numpy.zeros((PopSize, dim))
    fit = numpy.zeros(PopSize)
    M = numpy.zeros(PopSize)
    gBestScore = float("inf")

    pos = numpy.random.uniform(0, 1, (PopSize, dim)) * (ub - lb) + lb

    convergence_curve = numpy.zeros(iters)

    print("GSA is optimizing  \"" + objf.__name__ + "\"")

    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")

    for l in range(0, iters):
        for i in range(0, PopSize):
            l1 = [None] * dim
            l1 = numpy.clip(pos[i, :], lb, ub)
            pos[i, :] = l1

            # Calculate objective function for each particle
            fitness = objf(l1)
            fit[i] = fitness

            if (gBestScore > fitness):
                gBestScore = fitness

        """ Calculating Mass """
        M = massCalculation.massCalculation(fit, PopSize, M)

        """ Calculating Gravitational Constant """
        G = gConstant.gConstant(l, iters)

        """ Calculating Gfield """
        acc = gField.gField(PopSize, dim, pos, M, l, iters, G, ElitistCheck, Rpower)

        """ Calculating Position """
        pos, vel = move.move(PopSize, dim, pos, vel, acc)

        convergence_curve[l] = gBestScore

        if l % 1 == 0:
            print(['At iteration ' + str(l + 1) + ' the best fitness is ' + str(gBestScore)]);
    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.Algorithm = "GSA"
    s.objectivefunc = objf.__name__
    print("Execution time is for " + str(iters) + " iterations is : " + str(s.executionTime) + " seconds")

    return s
