stack = []
cek = {')':'(','}': '{', ']': '['}
text = input()
status = True

for temp in text:  
    if temp in cek.values(): 
        stack.append(temp)
    elif temp in cek.keys():  
        if stack and stack[-1] == cek[temp]:  
            stack.pop()
        else:
            status = False
            
if status == True:
    print(text + "\nvalid") 
else:
    print(text + "\ninvalid") 