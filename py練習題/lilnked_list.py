class stu:
    def __init__(self, ngfbf):
        self.ngfbf=ngfbf
        self.next=None

head=stu(None)
head.next=None
ptr=head

for _ in range(5):
    n=int(input())
    newstu=stu(n)
    newstu.next=None
    ptr.next=newstu
    ptr=ptr.next

ptr=head.next
while ptr.next!=None:
    print(ptr.ngfbf)
    ptr=ptr.next