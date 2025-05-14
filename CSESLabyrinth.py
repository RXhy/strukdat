import sys
from collections import deque
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
lab = []
for i in range(n):
    temp = input().strip()
    lab.append(temp)
    if 'A' in temp:
            sx,sy = i,temp.index('A')
    if 'B' in temp:
            ex,ey = i,temp.index('B')

# Directions: (dy, dx), direction letter
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
directions = ['U', 'D', 'L', 'R']

#visited
visited = [[False]*m for _ in range(n)]
parent = [[-1]*m for _ in range(n)]

#path finding BFS
q = deque()
q.append((sx, sy))
visited[sx][sy] = True

found = False
while q:
    x,y = q.popleft()
    if (x,y) == (ex,ey):
        found = True
        break
    
    for d in range(4):
        nx, ny = x + dx[d] , y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and lab[nx][ny] != '#':
            visited[nx][ny] = True
            parent[nx][ny] = d
            q.append((nx,ny))

if not found:
    print("NO")
else:
    print("YES")
    path = []
    x,y = ex, ey
    while (x,y) != (sx,sy):
        d = parent[x][y]
        path.append(directions[d])
        x -= dx[d]
        y -= dy[d]
    path.reverse()
    print(len(path))
    print("".join(path))