n = int(input())
mobil = list(map(int,input().split()))

stack= []
gang = []

stack.append(0)
gang.append(n+1)
for car in mobil:
    if car == stack[-1] + 1:
        stack.append(car)
    elif car > gang[-1]:
        gang.append(car)
    else:
        while gang[-1] == stack[-1] + 1:
            stack.append(gang.pop())
        if car != stack[-1]+1 or car > gang[-1]:
            ans = 0
if ans:
    print("yes")
else: 
    print("no")