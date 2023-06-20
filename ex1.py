from itertools import combinations
from grafo_a import *

#Find number of connected components

def count_connected_components(graph):
    visited = set()
    num_components = 0
    principal_comp_size = 0
    principal_comp_elements = []

    while(len(visited) < len(graph._graph)):
        for initial_vertex in graph._graph:
            if initial_vertex not in visited:
                component_stack = [initial_vertex]
                new_component_size = 0
                new_component_elements = []
                while component_stack:
                    vertex = component_stack.pop()
                    if vertex not in visited:
                        visited.add(vertex)
                        new_component_size += 1
                        new_component_elements.append(vertex)
                        if new_component_size > principal_comp_size:
                            principal_comp_size = new_component_size
                            principal_comp_elements = new_component_elements
                        for neighbor in graph.get_neighbors(vertex):
                            if neighbor not in visited:
                                component_stack.append(neighbor)
                num_components += 1

    return num_components, principal_comp_elements

# pc_num, pc_list = count_connected_components(graph)
# print(pc_num, len(pc_list))
    
