# Genetic Algorithm for Graph Partitioning

> ## a. Justification of why you have chosen your topic.
> Graph partioning is a one of the NP-hard combinatorial optimization problems. We can find many papers applying genetic algorithm to the graph partiioning problem.
> Among those papers, I decided to apply the method from the journal paper **"Genetic Algorithm and Graph Partitioning" written by Thang Nguyen Bui and Byung Ro Moon.** The method suggested in the paper can be applied to our term project with two reasons below. 
> 
> 1. The paper provides the description of the genetic algorithm and essential functions (mutation operator, crossover operator and else) for the graph partitioning.
> 
> 2. The paper contains the experiment, which can be conducted by beginner of graph partitioning problem, compared to other recent papers.
> 
> Moreover, I'm currently working on the topic related to graph, so this topic will be helpful to adapt GA to my research someday. Therefore, I choose this topic and the paper as the reference.
> 
> (Paper link: https://ieeexplore.ieee.org/abstract/document/508322)
>
>
> ## b. What is the topic?
> **Graph partitioning.**
> 
> To given an undirected graph G = (V, E) where V is the set of n nodes and E is the set of edges between the nodes, it divides the graph into two disjoint subsets of nodes partition1 and partition2 so that the number of edges between the nodes in the different subsets is minimized, and the sizes of the subsets are equal.
> 
> ## c. Design decision explaining why you select
>> ### Parameters
> There are 5 parameters in the program.
> 
> * **POP_SIZE**
>     * Initial population size
>     * Type : INT
>     * Range : [1, INF)
>     
> * **NUM_NODES**
>     * The number of nodes in the graph which will be generated randomly.
>     * It should be an **even number**.
>     * Type : INT
>     * Range : [2, INF)
>
> * **CONNECT_PROB**
>     * The probability to connect two nodes with edge
>     * Type : FLOAT
>     * Range : [0., 1.)
>     
> * **MUT_PROB**
>     * The probability to execute mutation
>     * Type : FLOAT
>     * Range : [0., 1.)
>     
> * **STOPPING_COUNT**
>     * Stopping criteria
>     * If there is no improvement within STOPPING_COUNT times, the program will be terminated.
>     * Type : INT
>     * Range : (1, INF)
>
> * **K_IND**
>     * How many individuals are selected for the tournament
>     * Type : INT
>     * Range : [1, NUM_NODES)
> -----    
>> ### Stopping criteria
> * If there's **no improvement within 20 times**, the program will be terminated.
> * How many times you accept it without the improvement can be adjusted with the parameter _**STOPPING_COUNT**_.
> -----
>> ### Fitness function
> * Fitness of each individual will be calculated by the equation below.
> 
>     ![image](https://user-images.githubusercontent.com/39353959/144560378-1a212d1c-31d5-47ef-b454-26152de7df78.png)
> 
>     * ![image](https://user-images.githubusercontent.com/39353959/144559997-3e08aae1-870f-4f67-a792-2005a7bf3bfb.png) : cut size of the worst solution in the population
>     * ![image](https://user-images.githubusercontent.com/39353959/144560079-36b87173-76a5-488a-ac56-1296ba0945bf.png) : cut size of the best solution in the population
>     * ![image](https://user-images.githubusercontent.com/39353959/144560056-0ce62c13-045b-4950-b04c-b6d113fae90d.png) : cut size of solution i.
> 
>     The cut is the set of edges between the partitions.
> 
> -----
>> ### Selection operator
> * **Tournament selection**
>     * Select k random individuals from the population and pick the best out of them
>     * random number k can be adjusted with the parameter _**K_IND**_
>     
>     ![image](https://user-images.githubusercontent.com/39353959/144561003-982bf85d-bd1b-41ef-a729-c76ed59bbea8.png)
>     
>     (© https://medium.com/pragmatic-programmers/implementing-common-selection-strategies-37c6f99795a6)
> -----
>> ### Crossover operator
> **I replaced single point crossover to multi-point crossover.**  
> However, a single point crossover is still available.
> 
> * **Multi-point crossover**
>     * From the tournament selection, two chromosomes are selected as parents.
>     * 5 cut points for crossover are selected randomly
>     * Offspring 1 and 2 will be generated in **different way** (described in below image).
>     * If the partitions of new offspring don't have the same size, the offspring will be **discarded**
>
>     ![image](https://user-images.githubusercontent.com/39353959/145143001-adfedeac-33a1-42cd-8c68-956a236716b6.png)
>
> * ~~**Single point crossover**~~
>     * ~~From the tournament selection, two chromosomes are selected as parents.~~
>     * ~~The crossover point is selected randomly.~~
>     * ~~If the partitions of new offspring don't have the same size, the offspring will be **discarded**.~~
>
> -----
>> ### Mutation operator
> * Replace one node in a graph with a different, compatible type.
> * The node randomly chosen from partition 0 will be exchanged with the node randomly chosen from partition 1.
>
>![image](https://user-images.githubusercontent.com/39353959/144572243-bfc91655-baa3-436b-b1c5-aa941762bd38.png)
>
> -----
>> ### Generational selection strategy
> * **Elitism**
>     * Maintaining M best individuals from the parents' generation
> ## d. How to run your project.
> ```
> cd src
> python3 main.py
> ```
>> ### Requirements
> ```
> python 3.x
> networkx
> numpy
> ```
>> **Installation**
>> ```
>> pip install networkx
>> pip3 install numpy
>> ```
> ## e. How to adjust parameters.
> Parameters are defined as global variables in main.py.
> ```
> POP_SIZE = 300 
> NUM_NODES = 100
> CONNECT_PROB = 0.3
> MUT_PROB = 0.05
> STOPPING_COUNT = 20
> K_IND = int(POP_SIZE * 0.1)
> ```
> You can adjust the parameters by modifying the values of them.
> 
