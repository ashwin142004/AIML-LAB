from queue import PriorityQueue

v = 14  # Number of vertices
graph = [[] for _ in range(v)]

# Example heuristic values for each node (h(n)), assuming target is node 9
heuristics = [10, 8, 5, 7, 3, 6, 4, 2, 1, 0, 3, 6, 5, 4]  

def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((heuristics[actual_Src], actual_Src))  # Use heuristic for priority
    visited[actual_Src] = True
    
    while not pq.empty():
        _, u = pq.get()  # Extract the node with the lowest heuristic value
        print(u, end=" ")
        
        if u == target:
            break

        for v, _ in graph[u]:  # Ignore edge cost
            if not visited[v]:
                visited[v] = True
                pq.put((heuristics[v], v))  # Use heuristic for priority
    print()

# Function to add undirected edges
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

# Sample Graph Edges
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

source = 0
target = 9
best_first_search(source, target, v)
