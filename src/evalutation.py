"""
evalutation.py --- Calculating fitness and cut size
- calCut: calculating cut size of all individuals in population to get best cut size and worst cut size
- fitness: fitness function using cut sizes
"""


def calCut(pop, g):
    cuts = []

    for ind in pop:
        part0 = [index for index in range(len(pop[0])) if ind[index] == 0]  # partition 0
        part1 = [index for index in range(len(pop[0])) if ind[index] == 1]  # partition 1

        g0 = g.subgraph(part0)
        g1 = g.subgraph(part1)

        cutSize = len(g.edges()) - (len(g0.edges()) + len(g1.edges()))
        cuts.append(cutSize)

    bestCut = min(cuts)
    worstCut = max(cuts)

    return bestCut, worstCut


def fitness(worstCut, bestCut, ind):
    part0 = [index for index in range(len(ind)) if ind[index] == 0]  # partition 0
    part1 = [index for index in range(len(ind)) if ind[index] == 1]  # partition 1

    g0 = g.subgraph(part0)
    g1 = g.subgraph(part1)

    curCut = len(g.edges()) - (len(g0.edges()) + len(g1.edges()))

    value = (worstCut - curCut) + (worstCut - bestCut) / 3  # fitness calculation

    return value, curCut