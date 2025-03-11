stack = []
cek = {')':'(','}': '{', ']': '['}
n= int(input())
status = True

for i in range(n):
    temp = input()
    if temp in cek.values():
        stack.append(temp)
    elif temp in cek.keys():
        if temp not in stack:
            stack.append(temp)
            status = False
if status == True:
    print(*stack)
    print("valid") 
else:
    print(*stack)
    print("invalid") 
# check [({)] invalid / [()] valid