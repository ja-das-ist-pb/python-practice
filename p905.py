import math

a=int(input())
sa=math.sqrt(a)
ca=math.cbrt(a)
primea=a+1
got=False
while got==False:
    got=True
    for i in range(2, int(math.sqrt(primea))+1):
        if primea%i==0:
            got=False
            break
    if got==False:
        primea+=1
    else:
        break
print(primea, (int(sa)+1)**2, (int(ca)+1)**3)