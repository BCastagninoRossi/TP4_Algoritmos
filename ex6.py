from grafo_a import *
from ex1 import count_connected_components
from collections import deque
import time
from tqdm import tqdm
import random

# def find_diameter_with_weights(graph, pc_element_list):
#     max_diam = 0
#     for element in pc_element_list:
#         dictionary = dijkstra(graph, element)
#         for key in dictionary.keys():
#             if dictionary[key] > max_diam:
#                 max_diam = dictionary[key]
#     return max_diam

def depth_dict_bfs(graph, initial_vertex):
    queue = deque()
    visited = set()
    distance = 0
    queue.append((initial_vertex, 0))
    while len(queue) > 0:
        vertex, distance  = queue.popleft()
        for neighbour in graph.get_neighbors(vertex):
            if neighbour not in visited:
                queue.append((neighbour, distance +1))
                visited.add(neighbour)
    return distance

# def find_diameter_no_weights(graph, pc_element_list):
#     max_dist = 0
#     total_elements = len(pc_element_list)

#     start_time = time.time()
#     for index, element in enumerate(tqdm(pc_element_list, desc="Progress", unit="element")):
#         depth = max_depth_bfs(graph, element)
#         if depth > max_dist:
#             max_dist = depth

#         elapsed_time = time.time() - start_time
#         avg_time_per_element = elapsed_time / (index + 1)
#         remaining_elements = total_elements - (index + 1)
#         estimated_time_remaining = avg_time_per_element * remaining_elements

#         print(f"Estimated time remaining: {estimated_time_remaining:.2f} seconds")

#     return max_dist

def find_diameter_no_weights_max15min(graph, pc_element_list):
    max_dist = 0
    num_components = len(pc_element_list)
    start_time = time.time()
    visited = set()

    for i in range(num_components):
        index = random.randint(0, num_components-1)
        if pc_element_list[index] in visited:
            continue
        visited.add(pc_element_list[index])
        depth = depth_dict_bfs(graph, pc_element_list[index])
        if depth > max_dist:
            max_dist = depth

        elapsed_time = time.time() - start_time
        if elapsed_time >= 900:  
            break

    return max_dist

principal_comp_num, principal_comp_elements = count_connected_components(graph)
pc_diameter = find_diameter_no_weights_max15min(graph, principal_comp_elements)
print("Principal component diameter is (ESTIMATE AFTER 15min): ")
print(pc_diameter)


#Tiempo estimado para cálculo exacto de diámetro: 12 días
#Diámetro estimado (tras 15 minutos): 20



