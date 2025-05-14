n = int(input())
day = list(map(int,input().split()))
wait = []

for i in range(len(day)):
    time = 0  
    current = day.pop(0)
    queue = day[:]
    temptime = 0 
    while queue:
        next = queue.pop(0)
        if current > next:
            temptime += 1
        if current < next:
            time += 1
            time += temptime
            break
    wait.append(time)
    
print(*wait)