import matplotlib.pyplot as plot
import networkx as nx

G = nx.Graph()  # new graph

# academic buildings
G.add_node('Alison')
G.add_node('Brown')
G.add_node('Colburn')
G.add_node('Ewing')
G.add_node('Gore')
G.add_node('ISE')
G.add_node('Hartshorn')
G.add_node('Kirkbride')
G.add_node('McDowell')
G.add_node('Memorial')
G.add_node('Mitchell')
G.add_node('Old College')
G.add_node('Penny')
G.add_node('Pearson')
G.add_node('Purnell')
G.add_node('Sharp')
G.add_node('Smith')
G.add_node('Spencer')
G.add_node('Willard')

G.add_node('The Green')

# add edges (weight is distance in Meters)

# Connected to The Green
G.add_edge("Alison", "The Green", weight=39)
G.add_edge("Memorial", "The Green", weight=10)
G.add_edge("Brown", "The Green", weight=14)
G.add_edge("Mitchell", "The Green", weight=38)
G.add_edge("Gore", "The Green", weight=7)
G.add_edge("Sharp", "The Green", weight=11)
G.add_edge("Alison", "The Green", weight=31)
G.add_edge("Old College", "The Green", weight=132)
G.add_edge("Hartshorn", "The Green", weight=107)

G.add_edge("Brown", "Memorial", weight=51)
G.add_edge("Alison", "Memorial", weight=68)
G.add_edge("Alison", "ISE", weight=85)

G.add_edge("Old College", "Willard", weight=90)
G.add_edge("Old College", "McDowell", weight=37)
G.add_edge("Willard", "McDowell", weight=20)

G.add_edge("Willard", "Ewing", weight=186)
G.add_edge("Gore", "Smith", weight=44)
G.add_edge("Purnell", "Smith", weight=20)
G.add_edge("Ewing", "Smith", weight=56)
G.add_edge("Kirkbride", "Smith", weight=28)
G.add_edge("Kirkbride", "Purnell", weight=61)
G.add_edge("Kirkbride", "Ewing", weight=33)
G.add_edge("Ewing", "Purnell", weight=24)

G.add_edge("Colburn", "Spencer", weight=5)
G.add_edge("Colburn", "Pearson", weight=61)
G.add_edge("Spencer", "Pearson", weight=76)
G.add_edge("Colburn", "ISE", weight=58)
G.add_edge("ISE", "Brown", weight=176)
G.add_edge("ISE", "Penny", weight=61)
G.add_edge("Alison", "Penny", weight=97)

# draw graph
pos = nx.spring_layout(G, k=1, seed=16)
nx.draw(G, pos, with_labels=True, node_color="#d4e1ff",
        node_size=450, font_weight='bold')

# drawels on edges
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

# show graph
plot.show()
