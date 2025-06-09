n = int(input())
tinggi = list(map(int,input().split()))
stack = []
output = [-1]*n 

for i in range(n):
    curr = tinggi.pop()
    stack = tinggi[:]
    while stack and curr >= stack[-1]:
        stack.pop()
    output[n-1-i] = len(stack) - 1
    # print(i,curr,stack)

print(*output)