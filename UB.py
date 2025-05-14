stack = []
operator = "^*-+:"
output = []

exp = input().split()

for curr in exp:
    stack.append(curr)
    
    if curr.isdigit():
        output.append(curr)   
        
    elif curr == ")":
        while stack[-1] not in operator:
            stack.pop()
        output.append(stack[-1])
        stack.pop()

while stack:
    curr = stack.pop()
    if curr in operator:
        output.append(curr)
        
def postfix(text):
    stack = []
    for char in text:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == "+": stack.append(a + b)
            elif char == "-": stack.append(a - b)
            elif char == "*": stack.append(a * b)
            elif char == ":": stack.append(a / b)
    return print(int(stack[0]))

postfix(output)