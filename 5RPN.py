stack = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
operator = "^*-+/"
output = []

n = int(input())
for i in range(n):
    temp = input()
    stack.append(temp)
    
    if temp in alphabet:
        output.append(temp)   
             
    elif temp == ")":
        while stack[-1] not in operator:
            stack.pop()
        output.append(stack[-1])
        stack.pop()
    
for i in range(len(output)):
    print(output[i],end="")
#(a+(b*c)) = abc*+
#((a+b)*(z+x)) / ab+zx+*
#((a+t)*((b+(a+c))^(c+d))) / at+bac++cd+^*


