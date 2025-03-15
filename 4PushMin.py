stack = []
side = []
n = int(input())
for i in range(n):
    x =input().split(" ")
    
    if x[0] == "PUSH":
        value = int(x[1])
        stack.append(value)
        
        if len(side) == 0 or value < side[-1]:
            side.append(value)
        else:
            side.append(side[-1])
                
    elif x[0] == "POP":
        side.pop()
        stack.pop()
        
    elif x[0] == "MIN":
        print(side[-1])
        
    print(stack,side)