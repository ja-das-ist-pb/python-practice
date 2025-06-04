from collections import deque

def bfs(n, t, p, l, r):
    queue=deque()
    direction=[l, r]
    walked=set()
    queue.append((0, 0))
    walked.add(0)
    
    while queue:
        x, step=queue.popleft()
        if x==p:
            return step
        for d in direction:
            nx=x+d
            if 


n, p, l, r=map(int, input().split())
t=list(map(int, input().split()))
a=[x for x in range(5)]
print(bfs(n, t, p, l, r))