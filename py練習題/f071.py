lucky=[]*3
number=[]*5
money=[]*5
lucky=list(map(int, input().split()))
number=list(map(int, input().split()))
money=list(map(int, input().split()))
isthree=False
total=0
isexist=False

for i in range(5):
    if (number[i]==lucky[0]):
        total+=money[i]
    if (number[i]==lucky[2]):
        total+=money[i]
    if number[i]==lucky[2]:
        isthree=True
        isexist=True
    if isthree==True:
        total-=money[i]
        isthree=False
if isexist==True:
    total*=2
if total<0:
    print(0)
else:
    print(total)