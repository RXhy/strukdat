queue = []
n = int(input())
for i in range(n):
    temp = input()
    if "+" in temp:
        queue.append(int(temp[1:]))
    elif "-" in temp:
        if len(queue) > 0:
            queue.pop(0)
        else:
            break
print("empty") if len(queue) == 0 else print(queue)
