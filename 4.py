from grafo_a import *
import heapq

def dijkstra(graph, initial_vertex):
    #Creates "distances" dictionary where the keys are the vertexes of the graph and the values for each vertex is the distance from the root (initialized as infinity)
    distances = {vertex: float('inf') for vertex in graph._graph.keys()}
    #set root's distance to 0
    distances[initial_vertex] = 0

    #initialize a min heap so that each time we make a pop, it returns the vertex with the minimum distance to the root present in the heap at that time
    priority_queue = [(0, initial_vertex)]

    while priority_queue:
        #remove the min distance vertex from the heap 
        current_distance, current_vertex = heapq.heappop(priority_queue)

        for neighbor in graph.get_neighbors(current_vertex):
            weight = len(graph.get_edge_data(current_vertex, neighbor))
            distance = current_distance + weight

            # Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

dijkstra_dictionary = dijkstra(graph, "nm0000122")
print(dijkstra_dictionary["nm0289856"])