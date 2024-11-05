import os
import matplotlib.pyplot as plt
import networkx as nx

def save_graph_example(G, folder="graphs_examples", filename="graph_example.png", highlight_cliques=None):
    """
    Salva uma imagem do grafo `G` em formato PNG com posições e pesos dos vértices.
    Opcionalmente, pode destacar cliques específicos.

    Parameters:
    - G (nx.Graph): O grafo a ser visualizado.
    - folder (str): Pasta onde a imagem será salva.
    - filename (str): Nome do arquivo PNG a ser salvo.
    - highlight_cliques (list): Lista de cliques para destacar, cada clique é uma lista de nós.
    """
    # Cria a pasta se ela não existir
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Caminho completo para salvar a imagem
    filepath = os.path.join(folder, filename)

    positions = {node: G.nodes[node]['pos'] for node in G.nodes}
    labels = {node: G.nodes[node]['weight'] for node in G.nodes}
    
    plt.figure(figsize=(8, 8))
    
    # Desenhar o grafo base
    nx.draw(G, pos=positions, with_labels=True, labels=labels, node_size=500, font_size=10, font_color="white")
    
    # Destacar cliques se fornecidos
    if highlight_cliques:
        for clique in highlight_cliques:
            nx.draw_networkx_nodes(G, pos=positions, nodelist=clique, node_color='orange', node_size=600, alpha=0.8)
            nx.draw_networkx_edges(G, pos=positions, edgelist=[(clique[i], clique[j]) for i in range(len(clique)) for j in range(i+1, len(clique)) if G.has_edge(clique[i], clique[j])], width=3, edge_color="orange")

    # Salvar como PNG
    plt.savefig(filepath, format="png")
    plt.close()
