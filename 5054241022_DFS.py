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
def dfs(node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in adj.get(node,[]):
            dfs(neighbor)
dfs(0)