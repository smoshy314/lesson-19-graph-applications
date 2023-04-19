import networkx as nx
from networkx.algorithms import tree
import matplotlib.pyplot as plt



G = nx.read_weighted_edgelist("./PrimsGraphEdgeList.txt")
pos = nx.spring_layout(G, k=1, seed=10)
mst = nx.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
print(edgelist)

nx.draw(G,pos, with_labels=True, )
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.savefig('./test.png')

