def bfs(stx, sty, tarx, tary, barrier):
    

n=int(input())
barrier=[]
for _ in range(n):
    x, y=map(int, input().split())
    barrier.append((x, y))
stx, sty=map(int, input().split())
tarx, tary=map(int, input().split())
print(bfs(stx, sty, tarx, tary, barrier))