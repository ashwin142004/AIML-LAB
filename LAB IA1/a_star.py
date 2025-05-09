def a_star(start, goal):
    open_set = {start}
    closed_set = set()
    g = {start: 0}
    parents = {start: None}

    while open_set:
        current = min(open_set, key=lambda x: g[x] + heuristic(x))
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]
        
        open_set.remove(current)
        closed_set.add(current)
        
        for neighbor, cost in Graph[current]:
            if neighbor in closed_set:
                continue
            tentative_g = g[current] + cost
            if neighbor not in open_set or tentative_g < g.get(neighbor, float('inf')):
                parents[neighbor] = current
                g[neighbor] = tentative_g
                open_set.add(neighbor)
    
    return None

def heuristic(n):
    H = {'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0}
    return H[n]

Graph = {
    'A': [('B', 6), ('F', 3)], 
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)], 
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)], 
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)], 
    'H': [('I', 2)], 
    'I': [('E', 5), ('J', 3)]
}

print(a_star('A', 'J'))
