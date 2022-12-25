import time

import GSA as gsa
import benchmarks


def selector(algo, func_details, popSize, Iter):
    function_name = func_details[0]
    lb = func_details[1]
    ub = func_details[2]
    dim = func_details[3]

    if algo == 0:
        x = gsa.GSA(getattr(benchmarks, function_name), lb, ub, dim, popSize, Iter)
    return x


# Select optimizers
GSA = True

# Select benchmark function
F1 = True

Algorithm = [GSA]
objectivefunc = [F1]

# Select number of repetitions for each experiment. 
# To obtain meaningful statistical results, usually 30 independent runs 
# are executed for each algorithm.
Runs = 1

# Select general parameters for all optimizers (population size, number of iterations)
PopSize = 50
iterations = 30

# Export results ?
Export = True

# ExportToFile="YourResultsAreHere.csv"
# Automatically generated name by date and time
ExportToFile = "experiment" + time.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"

# Check if it works at least once
atLeastOneIteration = False

# CSV Header for the convergence
CnvgHeader = []

for l in range(0, iterations):
    CnvgHeader.append("Iter" + str(l + 1))

for i in range(0, len(Algorithm)):
    for j in range(0, len(objectivefunc)):
        if (Algorithm[i]) and (objectivefunc[j]):   # start experiment if an Algorithm and an objective function is selected
            for k in range(0, Runs):
                func_details = benchmarks.getFunctionDetails(j)
                x = selector(i, func_details, PopSize, iterations)
