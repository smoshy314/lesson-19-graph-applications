import networkx as nx
from networkx.algorithms import tree
import matplotlib.pyplot as plt



G = nx.read_weighted_edgelist("./PrimsGraphEdgeList.txt")
pos = nx.nx_agraph.graphviz_layout(G)
mst = nx.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
print(edgelist)

'''
f = open("demofile3.txt", "w")
f.write(edgelist)
f.close()
mst1 = nx.read_edgelist("demofile3.txt")
nx.draw(mst1,with_labels=True)
nx.draw_circular(G)

plt.savefig('./test.png')
'''
