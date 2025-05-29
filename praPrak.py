def NewTree():
    return dict()

def Add_Node(tree:dict, parent, child):
    if tree.get(parent) != None:
        tree[parent].append(child)
    else:
        tree[parent] = [child]
        
mytree = NewTree()
Add_Node(mytree,1,2)
Add_Node(mytree,1,3)
Add_Node(mytree,2,4)
Add_Node(mytree,2,5)
Add_Node(mytree,5,6)

print(mytree)

def CountHeight(tree:dict, parent):
    if tree.get(parent) == None or parent not in tree.keys():
        return 1
    max_child_height = 0
    for child in tree[parent]:
        child_height = CountHeight(tree,child)
        max_child_height = max(max_child_height,child_height)
    return 1 + max_child_height

print(CountHeight(mytree,1))
    