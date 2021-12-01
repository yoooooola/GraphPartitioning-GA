# Genetic Algorithm for Graph Partitioning

> ## a. Justification of why you have chosen your topic.
> Graph partioning is a one of the NP-hard combinatorial optimization problems. We can find many papers applying genetic algorithm to the graph partiioning problem.
> Among those papers, I decided to apply the method from the journal paper "Performance of a Genetic Algorithm for the Graph Partitioning Problem (2003)" written by K. Kohmoto et al. The method suggested in the paper can be applied to our term project with two reasons below. 
> 
> 1. The paper provides the description of the genetic algorithm and essential functions (mutation operator, crossover operator and else) for the graph partitioning.
> 
> 2. The paper contains the experiment, which can be conducted by beginner of graph partitioning problem, compared to other recent papers.
> 
> Moreover, I'm currently working on the topic related to graph, so this topic will be helpful to apply GA to my research someday. Therefore, I choose this topic and the paper as the reference.
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
> - Initial Population: 100
> - Number of nodes: 
> - Number of edges: 
> - Mutation Rate: 0.05
> - Number of fitness evaluations: 100
> - Crossover Rate: 
> - Number of random individuals in selection (k)
> ```
>> ### Stopping criteria.
> ```
> Fixed number of fitness evaluations.
> In this program, the number will be fixed as 100.
> ```
>> ### Fitness function.
> ```
> Fitness will be calculated by the cut size.
> The cut is the set of edges between the partitions.
> ```
>> ### Selection operator.
> ```
> Tournament selection
> : Select k random individuals from the population and pick the best out of them
> ```
>> ### Crossover operator.
> ```
> Offsprings inherit genes from their parents, but not in identical forms.
> ```
>> ### Mutation operator.
> ```
> Replacing one node in a tree with a different, compatible type
> : The node randomly chosen from partition 1 will be exchanged with the node randomly chosen from partition 2.
> ```
>> ### Generational selection strategy.
> ```
> Elitism
> : Maintaining M best individuals from the parents' generation
> ```
> ## d. How to run your project.
> ```
> python main.py
> ```
> ## e. How to adjust parameters.
> Parameters are defined as global variables in above of main.py.
> So if you want to adjust parameters, you can do it by modifying the values of each parameters.
> 
