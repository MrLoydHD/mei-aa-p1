from typing import Tuple
from graph.drawGraph import draw_graph
from utils.domainClasses import Clique
import networkx as nx

class SearchAlgorithm:

    def __init__(self, graph: nx.Graph):
        self.graph = graph

    def perform_search(self) -> Clique:
        raise NotImplemented()

    def draw_graph(self):
        draw_graph(self.graph)

    @staticmethod
    def print_results(clique: Clique, header: str):
        if clique is not None:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print()
            print(f" {header}")
            print()
            print(" Max Weight Clique:")
            print("  ", clique.vertices)
            print()
            print(" Max Weight:")
            print("  ", clique.weight)
            print()
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        else:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print()
            print(" No Cliques found...")
            print()
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
