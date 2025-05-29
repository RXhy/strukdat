def pohon():
    return dict()

def cangkok(tree:dict, parent, child):
    if tree.get(parent) != None:
        tree[parent].append(child)
    else:
        tree[parent] = [child]

def potong(tree:dict, x):
    for i in tree.keys():
        curr = tree[i]
        if x in curr:
            tree[i].remove(x)
    if x in tree.keys():
        tree.pop(x)
    
def CountHeight(tree:dict, parent):
    if tree.get(parent) == None or parent not in tree.keys():
        return 1
    max_child_height = 0
    for child in tree[parent]:
        child_height = CountHeight(tree,child)
        max_child_height = max(max_child_height,child_height)
    return 1 + max_child_height
    

M = int(input())
d = list(map(int,input().split()))
q = int(input())
totalheight = 0 
wit = pohon()
for _ in range(q):
    temp= input().split()
    if temp[0] == "cangkok":
        cangkok(wit,int(temp[1]),int(temp[2])) 
    elif temp[0] == "potong":
        potong(wit,int(temp[1]))
    elif temp[0] == "siram":
        totalheight += 1

print(CountHeight(wit,d[0])+totalheight)