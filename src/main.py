import networkx as nx
import random as rd
from functools import partial
import time
import sys
import copy
from src.utils import initGraph, genPopulation
from src.evalutation import fitness, calCut
from src.operation import tournament, mutation, crossover

POP_SIZE = 500
NUM_NODES = 150  # SHOULD BE AN EVEN NUMBER !!!
MUT_PROB = 0.05
STOPPING_COUNT = 20
K_IND = int(POP_SIZE * 0.25)  # tournament size: K individual

"""
There're two ways to generate random graph.
You can choose the way you want. It generates the graph in similar way.

1. initGraph() from utils.py
2. nx.gnp_random_graph from networkX library
"""

g = initGraph(NUM_NODES)
# g = nx.gnp_random_graph(NUM_NODES, 0.6)
nx.draw(g)  # draw current graph

start_time = time.time()
pop = genPopulation(NUM_NODES, POP_SIZE)

# keep best values
bestSoFar = sys.maxsize
bestCutSize = sys.maxsize
bestPartition = []

bestCut, worstCut = calCut(pop, g)
eval_with = partial(fitness, worstCut, bestCut)

sortedPop = copy.deepcopy(sorted(pop, key=eval_with, reverse=True))
pop = copy.deepcopy(sortedPop)

genCount = 1
improveCount = 0

# stopping criteria; no improvement within STOPPING_COUNT then stop
while improveCount < STOPPING_COUNT:
    print("==================================================")
    print("Generation : ", genCount)
    print("Elapsed Time : ", time.time() - start_time)
    print("Population Size : ", len(pop))
    genCount = genCount + 1

    # fitness (high is good)
    currentFit, currentCut = fitness(worstCut, bestCut, pop[0])

    # print("Best Cut, Worst Cut, Current Cut: ", bestCut, worstCut, currentCut)

    # update best-so-far
    if currentFit < bestSoFar:
        improveCount = 0
        bestSoFar = currentFit
        bestCutSize = currentCut
        bestPartition = pop[0]

        print("==================================================")

        print("Best Partition : ", bestPartition)
        print("Best Cut Size : ", bestCutSize)
        print("Best So Far (Fitness) : ", bestSoFar)

    # no improvement
    else:
        improveCount += 1

    nextPop = copy.deepcopy(pop)

    # crossover
    for idx in range(int(POP_SIZE / 2)):
        parent1, parent2 = tournament(pop, bestCut, worstCut, K_IND)
        offspring1, offspring2 = crossover(parent1, parent2)

        if offspring1 not in nextPop and offspring1.count(0) == NUM_NODES / 2:
            nextPop.append(offspring1)
        if offspring2 not in nextPop and offspring2.count(0) == NUM_NODES / 2:
            nextPop.append(offspring2)

    # mutation
    for idx in range(len(nextPop)):
        randomProb = rd.random()
        if randomProb < MUT_PROB:
            mutInd = mutation(nextPop[idx])
            if mutInd not in nextPop:
                nextPop.append(mutInd)

    # update eval_with
    bestCut, worstCut = calCut(pop, g)
    # print("Best Cut, Worst Cut : ", bestCut, worstCut)
    eval_with = partial(fitness, worstCut, bestCut)

    pop = copy.deepcopy(sorted(nextPop, key=eval_with, reverse=True))
    pop = pop[:POP_SIZE]

print("-----SUMMARY-----")
print("Total Elapsed Time : ", time.time() - start_time)
print("Best So Far (Fitness) : ", bestSoFar)
print("Best Cut Size : ", bestCutSize)
print("Best Partition : ", bestPartition)

