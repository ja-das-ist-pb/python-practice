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

def preorder(ptr):
    if ptr!=None:
        print(ptr.val, end="")
        preorder(ptr.left)
        preorder(ptr.right)

def inorder(ptr):
    if ptr!=None:
        inorder(ptr.left)
        print(ptr.val, end="")
        inorder(ptr.right)

def postorder(ptr):
    if ptr!=None:
        postorder(ptr.left)
        postorder(ptr.right)
        print(ptr.val, end="")

print('DLR')
preorder(ptr)
print('------------------------')
print('LDR')
inorder(ptr)
print('------------------------')
print('LRD')
postorder(ptr)
# 5 6 24 8 12 3 17 1 9