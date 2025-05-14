n, e = map(int,input().split()) # node, edges 

adj = dict()

for i in range(e):
    a,b = map(int,input().split())
    adj[i] = [a,b]

for _ in range(e):
    print(f"{_}: {adj[_]}")