num, lim = map(int,input().split())
initiate = []
stack = []

for i in range (num):
    temp = int(input())
    if temp == lim:
        break
    else:
        initiate.append(temp)

for i in initiate:
    tempStack= []
    while stack and stack[-1] > i:
        tempStack.append(stack.pop())
    stack.append(i)
    while tempStack:
        stack.append(tempStack.pop())
print(stack)
        
    
 