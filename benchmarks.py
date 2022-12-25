import numpy


def F1(x):
    """ Spere Function """
    s = numpy.sum(x ** 2);
    return s


def getFunctionDetails(a):
    # [name, lb, ub, dim]
    param = {0: ["F1", -100, 100, 30],
             }
    return param.get(a, "nothing")
