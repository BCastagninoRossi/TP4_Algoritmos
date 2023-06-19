from grafo_b import *

def max_bacon_num(graph, actor1 = "nm0000102"):
    queue = []
    visited = set()
    distance = 0

    max_distance = 0
    max_actor = None

    queue.append((actor1, 0))

    while len(queue) > 0:
        vertex, distance  = queue.pop(0)
        for neighbour in graph.get_neighbors(vertex):
            if neighbour not in visited:
                queue.append((neighbour, distance +1))
                visited.add(neighbour)
                if distance+1 > max_distance:
                    max_distance = distance + 1
                    max_actor = neighbour

    return int(max_distance/2), max_actor

max_distance, max_actor = max_bacon_num(graph)
print("Max actor")
print(max_actor)
print("Max distance")
print(max_distance)