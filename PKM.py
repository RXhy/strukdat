n = int(input())
day = list(map(int,input().split()))
wait = [0]*n
stack = []

for i, k in enumerate(day):  
    while stack and day[stack[-1]] < k:
        prevInd = stack.pop()
        wait[prevInd] = i - prevInd
    stack.append(i)
    # print(i,k,stack,wait)

print(*wait)