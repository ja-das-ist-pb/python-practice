class tree:
    def __init__(self):
        self.val=None
        self.left=None
        self.right=None

def make_tree(root, val):
    newnode=tree()
    
    if root==None:
        newnode.val=val
        root=newnode
        return root
    
    else:
        current=root
        while current!=None:
            backup=current
            if val<current.val:
                current=current.left
            else:
                current=current.right
        if val<backup.val:
            newnode.val=val
            backup.left=newnode
            return root
        else:
            newnode.val=val
            backup.right=newnode
            return root

data=list(map(int, input().split()))
root=None
ptr=None
for i in range(len(data)):
    ptr=make_tree(ptr, data[i])

root=ptr
ptr=root.left
print('left node')
while ptr!=None:
    print(ptr.val)
    ptr=ptr.left
print()
print('right node')
ptr=root.right
while ptr!=None:
    print(ptr.val)
    ptr=ptr.right

# 5 6 24 8 12 3 17 1 9