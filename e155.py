from collections import deque

queue=deque()
discard=[]

while True:
    n=int(input())
    if n==0: break
    for i in range(1, n+1):
        queue.append(i)
    while len(queue)>1:
        discard.append(queue.popleft())
        queue.append(queue.popleft())
    
    print("Discarded cards:", ", ".join(map(str, discard)))
    print("Remaining card:", queue[0])
    queue.clear()
    discard.clear()