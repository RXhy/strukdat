n, e = map(int,input().split()) # node, edges 

adj = dict()

for i in range(e):
    a,b = map(int,input().split())
    if a in adj:
        adj[a].append(b)
    else:
        adj[a] = [b]
    if b in adj:
        adj[b].append(a)
    else:
        adj[b] = [a]

visited = set()
queue  = []

def bfs(node):
    queue.append(node)
    visited.add(node)
    
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for neighbor in adj.get(node,[]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)   
bfs(0)