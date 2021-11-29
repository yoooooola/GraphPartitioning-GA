# README

> ## a. Justification of why you have chosen your topic.
> Graph partioning is a one of the NP-hard combinatorial optimization problems. We can find many papers applying genetic algorithm to the graph partiioning problem.
> Among those papers, I try to apply the method from the journal paper "Performance of a Genetic Algorithm for the Graph Partitioning Problem (2003)" written by K. Kohmoto et al. The method suggested in the paper can be applied to our term project with two reasons below. 
> 
> 
> 1. The paper provides the description of the genetic algorithm and essential functions (mutation operator, crossover operator and else) for the graph partitioning.
> 
> 2. The paper contains the experiment, which can be conducted by beginner of graph partitioning problem, compared to other recent papers.
> 
> Moreover, I'm currently working on the topic related to graph, so this topic will be helpful to apply GA to my research someday.
> 
> Therefore, I choose this topic and the paper as the reference.
> 
> (Paper link: https://www.sciencedirect.com/science/article/pii/S0895717703901348)
>
>
> ## b. What is the topic?
> **Graph partitioning.**
> 
> To given an undirected graph G = (V, E) where V is the set of n nodes and E is the set of edges between the nodes, it divides the graph into two disjoint subsets of nodes v1 and v2 so that the number of edges between the nodes in the different subsets is minimized, and the sizes of the subsets are equal.
> 
> ## c. Design decision explaining why you select
>> ### Parameters such as the size of an initial population.
> ```
> - Initial population: 100
> - Number of nodes: 
> - Number of edges: 
> - Probability of mutation: 0.05
> ```
>> ### Stopping criteria.
> ```
> If there is no improvement within 20 times, the program will be stopped.
> ```
>> ### Fitness function.
> ```
> Fitness will be calculated by the cut size. The cut is the set of edges between the partitions.
> ```
>> ### Selection operator.
> ```
> ??
> ```
>> ### Crossover operator.
> ```
> The number of all the offspring generated from the population is a half of population size.
> ```
>> ### Mutation operator.
> ```
> By the given probability, The node randomly chosen from partition 1 will be exchanged with the node randomly chosen from partition 2.
> ```
>> ### Generational selection strategy.
> ```
> ??
> ```
> ## d. How to run your project.
> ```
> python main.py
> ```
> ## e. How to adjust parameters.
