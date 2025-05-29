node = list(map(int,input().split()))
curr = 0
output = []

root = node.pop(0)
output.append(str(root))

for i in range(len(node)):
    curr = node[i]
    if curr > root:
        output.append(str(curr))
        root = curr
            
print("".join(output))