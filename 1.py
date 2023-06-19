from itertools import combinations
from grafo_a import *

#Find number of connected components

def count_connected_components(graph):
    visited = set()
    num_components = 0

    while(len(visited) < len(graph._graph)):
        for initial_vertex in graph._graph:
            if initial_vertex not in visited:
                component_stack = [initial_vertex]
                while component_stack:
                    vertex = component_stack.pop()
                    if vertex not in visited:
                        visited.add(vertex)
                        for neighbor in graph.get_neighbors(vertex):
                            if neighbor not in visited:
                                component_stack.append(neighbor)
                num_components += 1

    return num_components

print(count_connected_components(graph))
    
