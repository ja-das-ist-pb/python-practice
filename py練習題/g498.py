def bfs(n, m, t):
    queue=[]
    visited=set()
    visited.add(0)
    queue.append(0)
    while len(queue)>0:
        now=queue.pop(0)
        if now>t:
            break
        if now==t:
            return "YES"
        if now+n not in visited and now+n<=t:
            queue.append(now+n)
            visited.add(now+n)
        if now+m not in visited and now+m<=t:
            queue.append(now+m)
            visited.add(now+m)

    return "NO"

n, m, item=map(int, input().split())
a=list(map(int, input().split()))

for t in a:
    print(bfs(n, m, t))