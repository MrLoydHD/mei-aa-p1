import networkx as nx
from itertools import chain, combinations
from algorithms.searchAlgorithm import SearchAlgorithm
from utils.domainClasses import Clique

class ExhaustiveSearch(SearchAlgorithm):

    def __init__(self, graph: nx.Graph):
        super().__init__(graph)

    def perform_search(self) -> tuple[Clique | None, int, int]:
        performed_operations = 0
        tested_solutions = 0
        all_cliques_found = []

        # Gerar todos os subconjuntos de vértices, incluindo o vazio
        all_vertex_subsets = chain.from_iterable(combinations(self.graph.nodes, r) for r in range(len(self.graph.nodes) + 1))

        # Loop sobre todos os subconjuntos para garantir pesquisa exaustiva
        for vertex_subset in all_vertex_subsets:
            tested_solutions += 1  # Contabiliza cada subconjunto testado

            # Verificar se o subconjunto é um clique e contabilizar cada verificação
            vertice_subset_is_clique, clique_operations = self.is_clique(vertex_subset)
            performed_operations += clique_operations  # Incrementa operações de verificação de clique

            if vertice_subset_is_clique and len(vertex_subset) > 0:  # Ignora o clique vazio no resultado final
                # Calcular o peso do clique
                clique_weight = sum(self.graph.nodes[node]['weight'] for node in vertex_subset)
                performed_operations += 1  # Incrementa operação de soma de pesos

                new_clique = Clique(vertices=list(vertex_subset), weight=clique_weight)
                all_cliques_found.append(new_clique)

        # Selecionar o clique com o peso máximo, sem considerar o vazio
        max_clique = max(all_cliques_found, key=lambda clique: clique.weight, default=None)

        return max_clique, performed_operations, tested_solutions

    def is_clique(self, vertex_subset):
        """Verifica se o subset de vértices forma um clique completo e conta operações detalhadas."""
        clique_operations = 0  # Inicializar contagem de operações
        num_nodes = len(vertex_subset)

        # Caso trivial: Se o subset tem menos de 2 vértices, é automaticamente um clique
        if num_nodes < 2:
            return True, clique_operations

        # Verificar se todos os pares de vértices têm uma aresta entre eles
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                clique_operations += 1  # Incrementa uma operação por par verificado
                v1, v2 = vertex_subset[i], vertex_subset[j]

                # Verificar se há uma aresta entre v1 e v2
                if not self.graph.has_edge(v1, v2):
                    return False, clique_operations

        return True, clique_operations
