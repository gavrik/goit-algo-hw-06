from task1 import init_network
import networkx as nx

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())
    #print(unvisited)

    while unvisited:
        current_vertex = min(unvisited, key = lambda vertex: distances[vertex])
        #print(current_vertex)
        if distances[current_vertex] == float('infinity'):
            break
        for neighbor, weight in graph[current_vertex].items():
            w = weight['weight']
            #print(neighbor, " ", w)
            distance = distances[current_vertex] + w
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

def nx_dijkstra(graph, start):
    return nx.single_source_dijkstra_path_length(graph, source=start)

if __name__ == "__main__":
    G = init_network()
    
    print(dijkstra(G, 'A'))
    print(nx_dijkstra(G, 'A'))
