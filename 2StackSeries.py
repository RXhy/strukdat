stack = []
n = int(input())
for i in range(n):
    ins = input()
    if "+" in ins:
        stack.append(ins[1:])
        print(len(stack))
    elif "-" in ins and len(stack) > 0:
        print(stack.pop())
    else:
        print("-1")
        break
print(stack)
# +7 +8 +5 - - 