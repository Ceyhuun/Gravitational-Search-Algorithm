import numpy


def gConstant(l, iters):
    alfa = 20
    G0 = 100
    Gimd = numpy.exp(-alfa * float(l) / iters)
    G = G0 * Gimd
    return G
