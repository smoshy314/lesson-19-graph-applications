import networkx as nx

dfs_graph = nx.read_adjlist("dfs_adjacency_list.txt", create_using=nx.DiGraph)
topologically_sorted_nodes = [*nx.topological_sort(dfs_graph)]
print(topologically_sorted_nodes)
