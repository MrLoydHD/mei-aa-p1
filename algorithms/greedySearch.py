import networkx as nx
from algorithms.searchAlgorithm import SearchAlgorithm
from utils.domainClasses import Clique

# The implemented Greedy algorithm can be described briefly using the following sequence of steps:

# 1. Start with an empty list \( L \) to hold the vertices of the clique and initialize the maximum clique weight to zero.
   
# 2. Sort all vertices in the graph in descending order of their weights.

# 3. For each vertex in this sorted list, treat it as a potential starting point for a new clique:
#    - a. Initialize \( L \) with this starting vertex and set the initial clique weight to the weight of this vertex.
#    - b. Get all neighbors of this vertex to form a set of candidates for expanding the clique.
   
# 4. While there are candidates for expanding \( L \):
#    - a. Select the neighbor with the highest weight from the candidate set.
#    - b. Check if this selected vertex is connected to all vertices in \( L \) (to ensure it can form a clique with them).
#       - If it is, add this vertex to \( L \) and update the clique weight by adding the weight of this vertex.
#       - Update the candidate set to only include vertices that are neighbors of the newly expanded clique.
#       - If it is not connected to all vertices in \( L \), remove it from the candidate set and continue with the remaining candidates.
   
# 5. Repeat Step 4 until no more candidates can be added to \( L \).

# 6. Track the clique with the highest weight found across all iterations. If the current clique weight is greater than the maximum weight recorded, update the maximum weight and store \( L \) as the current maximum weight clique.

# 7. The list \( L \) contains the vertices of the approximate maximum weight clique. Sum the weights of all vertices in \( L \) to get the weight of this maximum weight clique.


class GreedySearch(SearchAlgorithm):

    def __init__(self, graph: nx.Graph):
        super().__init__(graph)

    def perform_search(self) -> tuple[Clique | None, int, int]:
        performed_operations = 0
        tested_solutions = 1  # Initialize with 1, as we only count the final clique as one solution
        max_clique = None
        max_clique_weight = 0

        # Start with the highest-weight vertex as the first candidate for the clique
        vertices_sorted = sorted(self.graph.nodes, key=lambda v: self.graph.nodes[v]['weight'], reverse=True)
        for starting_vertex in vertices_sorted:
            current_clique = [starting_vertex]
            current_weight = self.graph.nodes[starting_vertex]['weight']
            candidates = set(self.graph.neighbors(starting_vertex))

            # Expand clique
            while candidates:
                best_candidate = max(candidates, key=lambda v: self.graph.nodes[v]['weight'])
                is_valid = all(self.graph.has_edge(best_candidate, node) for node in current_clique)
                performed_operations += len(current_clique)  # Count operations for each edge check

                if is_valid:
                    current_clique.append(best_candidate)
                    current_weight += self.graph.nodes[best_candidate]['weight']
                    candidates = candidates.intersection(self.graph.neighbors(best_candidate))
                else:
                    candidates.remove(best_candidate)

            # Update max clique if the current clique has a higher weight
            if current_weight > max_clique_weight:
                max_clique_weight = current_weight
                max_clique = Clique(vertices=current_clique, weight=current_weight)

        return max_clique, performed_operations, tested_solutions


    def build_greedy_clique(self, starting_vertex) -> tuple[list[int], int, int]:
        """Constrói um clique começando do vértice inicial com base na heurística Greedy."""
        clique = [starting_vertex]
        clique_weight = self.graph.nodes[starting_vertex]['weight']
        operations = 1  # Inicializa com uma operação para somar o peso do vértice inicial

        # Obter vizinhos do vértice inicial
        candidates = set(self.graph.neighbors(starting_vertex))

        while candidates:
            # Selecionar o vizinho com o maior peso
            next_vertex = max(candidates, key=lambda v: self.graph.nodes[v]['weight'])
            operations += 1  # Contabiliza a operação de seleção do próximo vértice

            # Verificar se o próximo vértice é adjacente a todos os vértices do clique atual
            if all(self.graph.has_edge(next_vertex, v) for v in clique):
                clique.append(next_vertex)
                clique_weight += self.graph.nodes[next_vertex]['weight']
                operations += len(clique)  # Incrementa as operações para verificar a adjacência

                # Atualizar candidatos para incluir apenas vizinhos comuns
                candidates.intersection_update(self.graph.neighbors(next_vertex))
            else:
                candidates.remove(next_vertex)
                operations += 1  # Conta a operação de remoção do candidato

        return clique, clique_weight, operations
