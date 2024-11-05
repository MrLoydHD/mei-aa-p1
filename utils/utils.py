from functools import reduce
from itertools import combinations
from math import comb
from utils.domainClasses import Vertice, Edge


def powerset(iterable):

    all_subsets = []
    operation_count = 0

    for L in range(len(iterable) + 1):
        for subset in combinations(iterable, L):
            operation_count += 1
            all_subsets.append(subset)

    return all_subsets, operation_count


def is_clique(vertice_subset: list[Vertice], edges: list[Edge]) -> tuple[bool, int]:

    edges_found = []
    vertices_in_subset_count = len(vertice_subset)
    operations_count = 0

    if comb(vertices_in_subset_count, 2) > len(edges):
        return False, operations_count

    for edge in edges:
        if edge.v1 in vertice_subset and edge.v2 in vertice_subset and edge.v1 != edge.v2:
            if edge not in edges_found:
                edges_found.append(edge)
                operations_count += 1
                # print("Found Edge: ", temp_edge)

    """
    There is one edge for each choice of two vertices, therefore, the number of edges
    is equal to the combination of (n 2) i.e., from each n vertices choose 2
    """
    return len(edges_found) > 0 and len(edges_found) == comb(vertices_in_subset_count, 2), operations_count


def subset_weight_sum(vertices_subset: list[Vertice]):

    weight_sum = 0
    for vertice in vertices_subset:
        weight_sum += int(vertice.weight)
    return weight_sum


def get_vertice_neighbors(vertice: Vertice, edges: list[Edge]) -> tuple[list[Vertice], int]:

    neighbors = []
    operations_count = 0

    for edge in edges:
        operations_count += 1
        if edge.v1 == vertice:
            neighbors.append(edge.v2)
        if edge.v2 == vertice:
            neighbors.append(edge.v1)

    return neighbors, operations_count


def get_max_common_neighbor(vertices_list, edges) -> tuple[Vertice, int] | tuple[None, int]:

    neighbors_of_all_vertices = []
    operations_count = 0

    for vertice in vertices_list:
        neighbors = []
        operations_count = 0

        for edge in edges:
            operations_count += 1
            if edge.v1 == vertice:
                neighbors.append(edge.v2)
            if edge.v2 == vertice:
                neighbors.append(edge.v1)
        neighbors_of_all_vertices.append(neighbors)
        operations_count += 1

    neighbors_of_all_vertices = list(reduce(set.intersection,
                                            [set(item) for item in neighbors_of_all_vertices]))

    # Remove all vertices already in the list - to not create a loop
    for vertice in vertices_list:

        if vertice in neighbors_of_all_vertices:
            neighbors_of_all_vertices.remove(vertice)

        operations_count += 1

    if len(neighbors_of_all_vertices) > 0:
        return sorted(neighbors_of_all_vertices, key=lambda v: v.weight, reverse=True)[0], operations_count,
    else:
        return None, operations_count,
