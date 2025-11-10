from collections import deque

def kill(a):
    while len(a)>1:
        if a[0]%2==0:
            a.append(a[0])
            a.popleft()
            a.popleft()
        else:
            a.append(a[0])
            a.popleft()
    return a[0]
        
n=int(input())
a=deque(map(int, input().split()))
print(kill(a))