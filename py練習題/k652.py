class tree:
    def __init__(self):
        self.val=None
        self.left=None
        self.right=None

def make_tree(root, val):
    newnode=tree()
    newnode.val=val

    if root==None:
        root=newnode
        return newnode
    else:
        c=root
        while c!=None:
            backup=c
            if val<c.val:
                c=c.left
            else:
                c=c.right
        if val<backup.val:
            backup.left=newnode
        else:
            backup.right=newnode
        return root
    
def search(root, val):
    c=root
    f=c
    pre=c
    while pre.val!=val:
        f=c
        if val<c.val:
            c=c.left
        else:
            c=c.right
        pre=c
    print(val, f.val)
        
        

n=int(input())
a=list(map(int, input().split()))
root=None
for i in range(len(a)-1, -1, -1):
    root=make_tree(root, a[i])

a_sorted=sorted(a)
for i in range(len(a_sorted)):
    if a_sorted[i]==root.val:
        print(a_sorted[i], -1)
    else:
        search(root, a_sorted[i])