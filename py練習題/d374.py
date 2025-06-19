import sys

m=int(sys.stdin.readline())
a=[]
for i in range(1, m):
    if i**2%m==1:
        a.append(i)
print(len(a))
for i in a:
    print(i)