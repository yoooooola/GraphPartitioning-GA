import networkx as nx
import matplotlib.pyplot as plt
import random as rd
from functools import partial
import time
import sys
import copy
from utils import genPopulation, initGraph
from operation import mutation, crossover

# Global variables
POP_SIZE = 300
NUM_NODES = 50  # SHOULD BE AN EVEN NUMBER !!!
MUT_PROB = 0.05
STOPPING_COUNT = 20
K_IND = int(POP_SIZE * 0.1)  # tournament size: K individual

# Generate random graph
# 1. initGraph(NUM_NODES)
# 2. nx.gnp_random_graph from networkX library
g = initGraph(NUM_NODES)
# g = nx.gnp_random_graph(NUM_NODES, 0.6)

# draw current graph
nx.draw(g)

# Calculate cut size 
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


# Calculate fitness
def fitness(worstCut, bestCut, ind):
    part0 = [index for index in range(len(ind)) if ind[index] == 0]  # partition 0
    part1 = [index for index in range(len(ind)) if ind[index] == 1]  # partition 1

    g0 = g.subgraph(part0)
    g1 = g.subgraph(part1)

    curCut = len(g.edges()) - (len(g0.edges()) + len(g1.edges()))

    value = (worstCut - curCut) + (worstCut - bestCut) / 3  # fitness calculation

    return value, curCut


# Selection operator: tournament selection
def tournament(pop, bestCut, worstCut):
    copiedPop = copy.deepcopy(pop)

    # tournament for parent 1
    candidates = rd.choices(copiedPop, k=K_IND)
    bestFit = sys.maxsize
    bestIdx = 0

    for idx in range(len(candidates)):
        currentFit, _ = fitness(worstCut, bestCut, pop[idx])
        if bestFit < currentFit:
            bestFit = currentFit
            bestIdx = idx

    copiedPop.remove(copiedPop[bestIdx])
    parent1 = copiedPop[bestIdx]

    # tournament for parent 2
    candidates = rd.choices(copiedPop, k=K_IND)
    bestFit = sys.maxsize
    bestIdx = 0

    for idx in range(len(candidates)):
        currentFit, _ = fitness(worstCut, bestCut, pop[idx])
        if bestFit < currentFit:
            bestFit = currentFit
            bestIdx = idx

    parent2 = copiedPop[bestIdx]

    return parent1, parent2


# MAIN
def main():
    start_time = time.time()

    # Generate population
    pop = genPopulation(NUM_NODES, POP_SIZE)

    # Variables to keep best values
    bestSoFar = sys.maxsize
    bestCutSize = sys.maxsize
    bestPartition = []

    bestCut, worstCut = calCut(pop, g)
    eval_with = partial(fitness, worstCut, bestCut)

    sortedPop = copy.deepcopy(sorted(pop, key=eval_with, reverse=True))
    pop = copy.deepcopy(sortedPop)

    genCount = 1
    improveCount = 0

    # Genetic algorithm
    while improveCount < STOPPING_COUNT:
        print("==================================================")
        print("Generation : ", genCount)
        print("Elapsed Time : ", time.time() - start_time)
        print("Population Size : ", len(pop))
        genCount = genCount + 1

        # fitness (high is good)
        currentFit, currentCut = fitness(worstCut, bestCut, pop[0])

        # print("Best Cut, Worst Cut, Current Cut: ", bestCut, worstCut, currentCut)

        # Update best-so-far
        if currentFit < bestSoFar:
            improveCount = 0
            bestSoFar = currentFit
            bestCutSize = currentCut
            bestPartition = pop[0]

            print("==================================================")
            print("Best Partition : ", bestPartition)
            print("Best Cut Size : ", bestCutSize)
            print("Best So Far (Fitness) : ", bestSoFar)

        # No improvement
        else:
            improveCount += 1

        nextPop = copy.deepcopy(pop)

        # Crossover
        for idx in range(int(POP_SIZE / 2)):
            parent1, parent2 = tournament(pop, bestCut, worstCut)
            offspring1, offspring2 = crossover(parent1, parent2)

            if offspring1 not in nextPop and offspring1.count(0) == NUM_NODES / 2:
                nextPop.append(offspring1)
            if offspring2 not in nextPop and offspring2.count(0) == NUM_NODES / 2:
                nextPop.append(offspring2)

        # Mutation
        for idx in range(len(nextPop)):
            randomProb = rd.random()
            if randomProb < MUT_PROB:
                mutInd = mutation(nextPop[idx])
                if mutInd not in nextPop:
                    nextPop.append(mutInd)

        # Update eval_with
        bestCut, worstCut = calCut(pop, g)
        eval_with = partial(fitness, worstCut, bestCut)

        pop = copy.deepcopy(sorted(nextPop, key=eval_with, reverse=True))
        pop = pop[:POP_SIZE]

    # GA Summary
    print("-----SUMMARY-----")
    print("Total Elapsed Time : ", time.time() - start_time)
    print("Best So Far (Fitness) : ", bestSoFar)
    print("Best Cut Size : ", bestCutSize)
    print("Best Partition : ", bestPartition)


if __name__ == "__main__":
    main()
