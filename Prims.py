import networkx as nx
#from networkx.algorithms import tree
import matplotlib.pyplot as plt

G = nx.read_weighted_edgelist("./PrimsGraphEdgeList.txt")

mst = nx.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
print(edgelist)

pos = nx.spring_layout(G, k=10, seed=5)
nx.draw(G,pos, with_labels=True,node_shape="o", font_size=10, node_size=500, node_color="#d4e1ff", linewidths=.5 )
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels,font_size=8 )

plt.savefig('./AcedemicBuildingGraph.png')

