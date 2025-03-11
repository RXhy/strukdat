stack = []
n = int(input())
for i in range(n):
    ins = input()
    if "+" in ins:
        stack.append(ins[1:])
        print(len(stack))
    if "-" in ins:
        print(stack.pop())
print(stack)
# +7 +8 +5 - - 