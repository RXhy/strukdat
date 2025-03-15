#https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3139
text = input().strip()
queue =  []
tempqueue = []
flag = False   

for char in text:
    if char == "[":
        flag = True
    elif char == "]":
        flag= False
    elif flag: 
        queue.append(char)
    else:
        tempqueue.append(char)
queue += tempqueue
print("".join(queue))