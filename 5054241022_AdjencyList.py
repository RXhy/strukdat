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

for _ in range(n):
    print(f"{_}: {adj[_]}")