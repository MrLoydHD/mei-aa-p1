import networkx as nx
from algorithms.searchAlgorithm import SearchAlgorithm
from utils.domainClasses import Clique

class BacktrackingSearch(SearchAlgorithm):

    def __init__(self, graph: nx.Graph):
        super().__init__(graph)
        self.max_clique = None
        self.max_clique_weight = 0
        self.performed_operations = 0

    def perform_search(self) -> tuple[Clique | None, int, int]:
        # Sort vertices by weight descending to prioritize higher weights first
        vertices_sorted = sorted(self.graph.nodes, key=lambda v: self.graph.nodes[v]['weight'], reverse=True)
        self._backtrack([], 0, vertices_sorted)
        
        # Return the maximum clique found, number of operations, and number of solutions tested
        tested_solutions = 1  # In backtracking, we count only the final max clique as one solution
        return self.max_clique, self.performed_operations, tested_solutions

    def _backtrack(self, current_clique, current_weight, candidates):
        # If no candidates remain, we reached the end of this branch
        if not candidates:
            if current_weight > self.max_clique_weight:
                self.max_clique_weight = current_weight
                self.max_clique = Clique(vertices=current_clique[:], weight=current_weight)
            return
        
        # Prune the branch if the maximum possible weight is less than max found
        max_possible_weight = current_weight + sum(self.graph.nodes[v]['weight'] for v in candidates)
        if max_possible_weight <= self.max_clique_weight:
            return

        # Try including each candidate vertex one by one
        for i, vertex in enumerate(candidates):
            new_clique = current_clique + [vertex]
            new_weight = current_weight + self.graph.nodes[vertex]['weight']
            self.performed_operations += 1  # Count this operation
            
            # Filter the remaining candidates to those connected to the current clique
            new_candidates = [v for v in candidates[i + 1:] if all(self.graph.has_edge(v, u) for u in new_clique)]
            
            # Recursive call to expand the clique further
            self._backtrack(new_clique, new_weight, new_candidates)

