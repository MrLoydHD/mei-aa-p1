import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def draw_graph(G):
    # Extrair posições e rótulos dos nós diretamente do grafo G
    positions = {node: G.nodes[node]['pos'] for node in G.nodes}
    labels = {node: str(G.nodes[node]['weight']) for node in G.nodes}

    # Desenhar o grafo com rótulos e posições
    nx.draw(G, labels=labels, with_labels=True, node_size=300, width=2, font_size=10, pos=positions)
    plt.show()
    plt.close()

