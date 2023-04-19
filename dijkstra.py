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

# add edges (weight is distance in Meters)

# Connected to The Green
G.add_edge("Alison Hall", "The Green", weight=39)
G.add_edge("Memorial Hall", "The Green", weight=10)
G.add_edge("Brown Lab", "The Green", weight=14)
G.add_edge("Mitchell Hall", "The Green", weight=38)
G.add_edge("Gore Hall", "The Green", weight=7)
G.add_edge("Sharp Lab", "The Green", weight=11)
G.add_edge("Alison Hall", "The Green", weight=31)
G.add_edge("Old College Hall", "The Green", weight=132)
G.add_edge("Hartshorn Hall", "The Green", weight=107)

G.add_edge("Brown Lab", "Memorial Hall", weight=51)
G.add_edge("Alison Hall", "Memorial Hall", weight=68)
G.add_edge("Alison Hall", "Harker ISE Lab", weight=85)

G.add_edge("Old College Hall", "Willard Hall", weight=90)
G.add_edge("Old College Hall", "McDowell Hall", weight=37)
G.add_edge("Willard Hall", "McDowell Hall", weight=20)

G.add_edge("Willard Hall", "Ewing Hall", weight=186)
G.add_edge("Gore Hall", "Smith Hall", weight=44)
G.add_edge("Purnell Hall", "Smith Hall", weight=20)
G.add_edge("Ewing Hall", "Smith Hall", weight=56)
G.add_edge("Kirkbride Hall", "Smith Hall", weight=28)
G.add_edge("Kirkbride Hall", "Purnell Hall", weight=61)
G.add_edge("Kirkbride Hall", "Ewing Hall", weight=33)
G.add_edge("Ewing Hall", "Purnell Hall", weight=24)

G.add_edge("Colburn Lab", "Spencer Lab", weight=5)
G.add_edge("Colburn Lab", "Pearson Hall", weight=61)
G.add_edge("Spencer Lab", "Pearson Hall", weight=76)
G.add_edge("Colburn Lab", "Harker ISE Lab", weight=58)
G.add_edge("Harker ISE Lab", "Brown Lab", weight=176)
G.add_edge("Harker ISE Lab", "Penny Hall", weight=61)
G.add_edge("Alison Hall", "Penny Hall", weight=97)

# draw graph
pos = nx.spring_layout(G, k=400)
nx.draw(G, pos, with_labels=True)

# draw labels on edges
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

# show graph
plot.show()
