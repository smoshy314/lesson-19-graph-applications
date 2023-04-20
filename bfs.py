import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_adjlist("bfs_adjlist.txt")
result = [*nx.bfs_layers(G, "Russell_Hall_A")]
print(result)

options = {
    "node_size": 700,
    "font_size": 7,
    "edge_color": "grey",
    "node_shape": "o",
    "font_weight": "bold",
    "with_labels": True
}

nx.draw(G, **options)
plt.show()
