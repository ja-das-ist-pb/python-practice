n=int(input())
h=[0]*n
w=[0]*n
t=[0]*n
h=list(map(int, input().split()))
w=list(map(int, input().split()))
for i in range(n):
    t[i]=h[i]*w[i]
print(h[t.index(min(t))], w[t.index(min(t))])