num, lim = map(int,input().split())
initiate = []
sortQ = []
for i in range (num):
    temp = int(input())
    if temp == lim:
        continue
    else:
        initiate.append(temp)
print(initiate,sortQ)