n, e, type = map(int,input().split()) # node, edges, 0 (undirected) else (directed)

adj = [[ 0 for _ in range(n)] for _ in range(n)]

#undirected graph
def undic(adj,e):
    for x in range(e):
        a, b = map(int,input().split())
        adj[a][b] = 1
        adj[b][a] = 1

#directed graph
def direc(adj,e):
    for x in range(e):
        a, b = map(int,input().split())
        adj[a][b] = 1

if type == 0: 
    undic(adj,e)
else:
    direc(adj,e)

for _ in range(n):
    print(adj[_])