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
