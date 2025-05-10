import heapq

h = {'A': 10, 'B': 8, 'C': 5, 'D': 0, 'E': 3, 'F': 6, 'G': 5, 'H': 12, 'I': 2, 'J': 0}
graph = {
    'A': [('B', 6), ('F', 3)], 'B': [('C', 3), ('D', 2)], 'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)], 'E': [('I', 5), ('J', 5)], 'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)], 'H': [('I', 2)], 'I': [('E', 5), ('J', 3)], 'J': []
}

def a_star(graph, start, goal):
    pq = [(h[start], 0, start)]  # (f = h + g, g, node)
    parent, g_cost = {start: None}, {start: 0}
    visited = set()

    while pq:
        f, g, node = heapq.heappop(pq)
        if node == goal:
            path = []
            while node: path.append(node); node = parent[node]
            return path[::-1]
        if node in visited: continue
        visited.add(node)
        for nbr, w in graph[node]:
            new_g = g + w
            if nbr not in g_cost or new_g < g_cost[nbr]:
                g_cost[nbr] = new_g
                parent[nbr] = node
                heapq.heappush(pq, (new_g + h[nbr], new_g, nbr))
    return None

path = a_star(graph, 'A', 'J')
print(path if path else "No path found")
