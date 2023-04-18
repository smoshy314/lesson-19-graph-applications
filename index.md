# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:

- First member (email)
- Second member (email)
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

# First Problem Title

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
> - Input:
> - Output:

**Graph Problem/Algorithm**: DFS

**Setup code**:

```python
import networkx as nx

dfs_graph = nx.read_adjlist("dfs_adjacency_list.txt", create_using=nx.DiGraph)
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
topologically_sorted_nodes = [*nx.topological_sort(dfs_graph)]
print(topologically_sorted_nodes)
```

**Output**

```
['I', 'K', 'X', 'O', 'A', 'G', 'L', 'B', 'M', 'V', 'Y', 'F', 'P', 'Q', 'E', 'H', 'J', 'Z', 'U', 'T', 'R', 'D', 'W', 'N', 'S', 'C']
```

**Interpretation of Results**:
