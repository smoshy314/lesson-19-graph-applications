import matplotlib.pyplot as plot
import networkx as nx

G = nx.Graph()  # new graph

# academic buildings
G.add_node('Alison Hall')
G.add_node('Brown Lab')
G.add_node('Colburn Lab')
G.add_node('Ewing Hall')
G.add_node('Gore Hall')
G.add_node('Harker ISE Lab')
G.add_node('Hartshorn Hall')
G.add_node('Kirkbride Hall')
G.add_node('McDowell Hall')
G.add_node('Memorial Hall')
G.add_node('Mitchell Hall')
G.add_node('Old College Hall')
G.add_node('Penny Hall')
G.add_node('Pearson Hall')
G.add_node('Purnell Hall')
G.add_node('Sharp Lab')
G.add_node('Smith Hall')
G.add_node('Spencer Lab')
G.add_node('Willard Hall')

G.add_node('The Green')

# draw graph
pos = nx.spring_layout(G, k=400)
nx.draw(G, pos, with_labels=True)

# draw labels on edges
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

# show graph
plot.show()
