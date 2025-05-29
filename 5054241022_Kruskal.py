from functools import cmp_to_key

def comparator(a,b):
    return a[2] - b[2]

def kruskals_mst(V, edges):

    edges = sorted(edges,key=cmp_to_key(comparator))
    
    dsu = DSU(V)
    cost = 0
    count = 0
    for x, y, w in edges:
        
        if dsu.find(x) != dsu.find(y):
            dsu.union(x, y)
            cost += w
            count += 1
            if count == V - 1:
                break
    return cost
    
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1

vertex, e = map(int,input().split())
edges = []
for i in range(e):
    temp = list(map(int,input().split())) 
    edges.append(temp)
print(kruskals_mst(vertex, edges))

    