from task1 import init_network
from collections import deque

def DFS_algo(G, vertex, visited = None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for n in G[vertex]:
        if n not in visited:
            DFS_algo(G, n, visited)
    

def BFS_algo(G, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end = ' ')
        visited.add(vertex)
        queue.extend(set(G[vertex]) - visited)
    BFS_algo(G, queue, visited)

if __name__ == "__main__":
    G = init_network()
    
    print("=== DFS ===")
    DFS_algo(G, 'A')
    print("\n=== BFS ===")
    BFS_algo(G, deque(["A"]))
