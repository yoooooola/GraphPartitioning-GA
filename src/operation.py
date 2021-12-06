"""
operation.py --- Operators for Genetic Algorithm; generate new offsprings
- mutation: mutation operator, exchanging indices from each partitions
- crossover: crossover operator, single point crossover
"""

import random as rd
import copy


# Mutation
def mutation(ind):
    mutatedInd = copy.deepcopy(ind)

    part0 = [index for index in range(len(ind)) if mutatedInd[index] == 0]  # partition 0
    part1 = [index for index in range(len(ind)) if mutatedInd[index] == 1]  # partition 1

    mutIdx0 = rd.choice(part0)
    mutIdx1 = rd.choice(part1)

    # swap indices
    mutatedInd[mutIdx0], mutatedInd[mutIdx1] = mutatedInd[mutIdx1], mutatedInd[mutIdx0]

    return mutatedInd


# Single point cross-over
def crossover(parent1, parent2):
    pivot = rd.choice(range(len(parent1)))

    offspring1 = parent1[:pivot] + parent2[pivot:]
    offspring2 = parent2[:pivot] + parent1[pivot:]

    return offspring1, offspring2
