import numpy as np
import networkx as nx
from math import comb, floor

def generate_graph(v, p):
    n_mec = 108215
    np.random.seed(n_mec)
    num_edges = floor(comb(v, 2) * p)

    # Criar um grafo não direcionado
    G = nx.Graph()

    # Adicionar nós com pesos aleatórios
    for i in range(v):
        x = np.random.randint(1, 21)
        y = np.random.randint(1, 21)
        weight = np.random.randint(1, 50)
        G.add_node(i, pos=(x, y), weight=weight)

    # Adicionar arestas aleatórias até alcançar o número necessário
    edges = set()  # Usar um set para evitar duplicação
    while len(edges) < num_edges:
        v1 = np.random.randint(0, v)
        v2 = np.random.randint(0, v)

        # Garantir que não estamos a criar um loop (aresta para o próprio nó)
        if v1 != v2 and (v1, v2) not in edges and (v2, v1) not in edges:
            G.add_edge(v1, v2)
            edges.add((v1, v2))

    return G

def clique_weight(G, clique):
    """Calcula o peso total de um clique."""
    return sum(G.nodes[node]['weight'] for node in clique)

