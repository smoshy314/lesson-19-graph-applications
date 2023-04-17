import matplotlib.pyplot as plot
import networkx as nx

G = nx.DiGraph()  # new graph

# academic buildings
G.add_node('Alison Hall')
G.add_node('Brown Hall')

# add edges
G.add_edge("Alison Hall", "Brown Hall", weight=5)


# draw graph
pos = nx.spring_layout(G, k=10)  # For better example looking
nx.draw(G, pos, with_labels=True)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

# show graph
plot.show()
