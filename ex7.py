from grafo_a import *
from ex1 import count_connected_components
from collections import deque
import time
import random

def mean_separations(graph, initial_vertex):
    visited = {}
    queue = deque()

    queue.append((initial_vertex, 0))

    while len(queue) > 0:
        vertex, distance  = queue.popleft()
        for neighbour in graph.get_neighbors(vertex):
            if neighbour not in visited.keys():
                queue.append((neighbour, distance +1))
                visited[neighbour] = distance +1

    key_num = len(visited.keys())
    total_separation = 0
    for key in visited.keys():
        total_separation += visited[key]
    
    return total_separation/key_num

def mean_separations_all_components(graph, component_elements):
    n_components = len(component_elements)
    visited = set()
    counter = 0
    total = 0
    start_time = time.time()
    for i in range(n_components):
        index = random.randint(0, n_components-1)
        if index in set():
            continue
        visited.add(index)
        total += mean_separations(graph, component_elements[index])
        counter +=1
        if time.time()-start_time >= 900:
            break
    

    return total/counter



principal_comp_num, principal_comp_elements = count_connected_components(graph)
print(mean_separations(graph, "nm0289856"))
print("Average separation between all components of the graph (AFTER 15min): ")
print(mean_separations_all_components(graph, principal_comp_elements))