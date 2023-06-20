from grafo_b import *
from collections import deque

def distance_between_actors(graph, actor1, actor2):
    if actor1 == actor2:
        return 0

    queue = deque()
    visited = set()
    distance = 0

    queue.append((actor1, 0))

    while len(queue) > 0:
        vertex, distance  = queue.popleft()
        if vertex == actor2:
            #divido la distancia por 2 ya que de otra manera estaría contando cada película y cada actor como un nivel de separación cuando lo único que quiero contar son las películas entre ellos y defino que si ambos participaron en la misma película la distancia es 1
            return int(distance/2)
        for neighbour in graph.get_neighbors(vertex):
            if neighbour not in visited:
                queue.append((neighbour, distance +1))
                visited.add(neighbour)

    return -1

# print(distance_between_actors(graph, "nm0000102", "nm0289856"))

