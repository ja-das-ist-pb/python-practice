from math import *
n=int(input())
a=list(map(int, input().split()))
indicator=0
room=[0]*n

for i in range(n):
    if a[i]%6==0:
        room[i]=1
        indicator+=1
    elif a[i]%2==1 and a[i]%3!=0:
        room[i]=2
        indicator+=1
    elif sqrt(a[i])-int(sqrt(a[i]))==0 or (a[i]%2==0 and a[i]%7!=0):
        room[i]=3
        indicator+=1
    elif indicator>=2:
        room[i]=-1

minroom=min(room)
if minroom<0:
    minroom=0

for i in range(n):
    if room[i]==-1:
        room[i]=minroom

for i in range (n):
    print(room[i], end=" ")