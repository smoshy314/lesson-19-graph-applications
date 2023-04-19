# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:

- Michael Bocelli (mbocelli@udel.edu)
- Joshua Martinez (zenitram@udel.edu)
- Third member (email)
- Fourth member (email)

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# Order of Bus Charging Station Installation

**Informal Description**:
As the head of transportation for the University of Delaware, you have been
tasked with installing several charging stations for UD's new electric bus
program, which will provide a clean and efficient transportation system for
students. However, certain charging stations require that others
be installed before them, so that they may be dolly-chained on the same
power line. Determine a correct order of installation by performing a
topological sort (through implementing a DFS) on the directed, acyclic graph
of power stations.

> **Formal Description**:
>
> - Input: A directed, acyclic graph G(E,V), where E is the set of edges, and V is the set of vertices.
> - Output: A list of the vertices in V sorted in topological order.

**Graph Problem/Algorithm**: DFS

**Setup code**:

```python
import networkx as nx

dfs_graph = nx.read_adjlist("dfs_adjacency_list.txt", create_using=nx.DiGraph)
```

**Visualization**:

![Image goes here](dfs_graph.png)

**Solution code:**

```python
topologically_sorted_nodes = [*nx.topological_sort(dfs_graph)]
print(topologically_sorted_nodes)
```

**Output**

```
['Charger_I', 'Charger_K', 'Charger_X', 'Charger_O', 'Charger_A', 'Charger_G', 'Charger_L', 'Charger_B', 'Charger_M', 'Charger_V', 'Charger_Y', 'Charger_F', 'Charger_P', 'Charger_Q', 'Charger_E', 'Charger_H', 'Charger_J', 'Charger_Z', 'Charger_U', 'Charger_T', 'Charger_R', 'Charger_D', 'Charger_W', 'Charger_N', 'Charger_S', 'Charger_C']
```

**Interpretation of Results**:
The results demonstrate the order in which the charging stations must be installed before installing others. For instance,
to install Charger_C, all other chargers must be installed first in their respective order in the list. Since Charger_G comes
after Charger_A, then Charger_A must be installed first, and so on.

# Least amount of Track to build to deliever supplies to select buildings

**Informal Description**:
As the head of transportation for the University of Delaware, you have been tasked with implementing a 
track system to transport pertainant supplies between select academic buildings. Due to the high cost
of building the system and your tight budget you must lay the smallest amount of track needed to reach 
every building that needs supplies tracks can only be laid among certain predefined paths gievn to you
by your boss. Unfortunately your boss was lazy 

> **Formal Description**:
>
> - Input: A undirected graph G(E,V), where E is the set of edges, and V is the set of vertices.
> - Output: A list of the edges in E given as (V1, V2) that when put together create a minimum spanning tree.

**Graph Problem/Algorithm**: Prim's

**Setup code**:

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_weighted_edgelist("./PrimsGraphEdgeList.txt")
```

**Visualization**:

![Image goes here](AcedemicBuildingGraph.png)

**Solution code:**

```python
mst = nx.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
print(edgelist)
```

**Output**

```
[('ISE', 'Alison'), ('ISE', 'Pearson'), ('ISE', 'Memorial'), ('Memorial', 'Evans'), ('Evans', 'DuPont'), ('Evans', 'Drake'), ('Drake', 'Brown'), ('Evans', 'Hullihen'), ('Hullihen', 'Gore'), ('Gore', 'Sharp'), ('Sharp', 'Wolf'), ('Drake', 'Spencer'), ('Gore', 'Smith'), ('Alison', 'Morris_Library'), ('Alison', 'Penny'), ('Gore', 'Kirbride'), ('Kirbride', 'Ewing'), ('Smith', 'AmyE_DuPont'), ('AmyE_DuPont', 'Gore_Recital'), ('Kirbride', 'Willard'), ('Willard', 'McDowell')]
```

**Interpretation of Results**:
The results demonstrate the buildings in which the tracks must be built between in order to have the least amount of track. For example, given the first element of the list ('ISE', 'Alison') We would build a
track between those two buildings. After building all the tracks given by the output we would have created a graph between all buildings with the lowest length of track and no cycles aka the MST.