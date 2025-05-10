import heapq

h_dist = {'A': 10, 'B': 5, 'C': 2, 'D': 0}
graph = {'A': [('C', 4), ('B', 1)], 'B': [('A', 1), ('D', 1)],
         'C': [('D', 2), ('A', 4)], 'D': [('B', 1), ('C', 2)]}

def best_first_search(graph, start, goal):
    pq = [(h_dist[start], start)]
    visited, parent = set([start]), {start: None}
    while pq:
        _, node = heapq.heappop(pq)
        if node == goal:
            path = []
            while node: path.append(node); node = parent[node]
            return path[::-1]
        for nbr, _ in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                parent[nbr] = node
                heapq.heappush(pq, (h_dist[nbr], nbr))
    return None

path = best_first_search(graph, 'A', 'D')
print(path if path else "No path found")
