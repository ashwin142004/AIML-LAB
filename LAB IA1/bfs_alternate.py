def heurisitc(ch): 
  h_dist = { 
    'A': 10, 
    'B': 5, 
    'C': 2, 
    'D': 0 
  } 
  return h_dist[ch] 
graph_nodes = { 
  'A': [('C',4),('B',1)], 
  'B': [('A',1),('D',1)], 
  'C': [('D',2),('A',4)], 
  'D': [('B',1),('C',2)] 
} 
def reconstruct_path(parent, end): 
  path = [] 
  while parent[end] != None: 
    path.append(end) 
    end = parent[end] 
  path.append(end) 
  path.reverse() 
  return path 
import heapq 
def best_first_search(graph_nodes, start, end): 
  n = len(graph_nodes) 
  pq = [] 
  visited = {index: False for index in graph_nodes} 
  parent = {index: None for index in graph_nodes} 
  heapq.heappush(pq,(heurisitc(start),start)) 
  visited[start] = True 
  while pq: 
    h, current =  heapq.heappop(pq) 
    if current == end: 
      return reconstruct_path(parent,end) 
    for neighbor, weight in graph_nodes[current]: 
      if not visited[neighbor]: 
        parent[neighbor] = current 
        visited[neighbor] = True 
        heapq.heappush(pq,(heurisitc(neighbor),neighbor)) 
  return None 
 
path = best_first_search(graph_nodes,'A','D') 
if(path): 
  print(path) 
else: 
  print('No path found') 