import sys

for i in sys.stdin:
    n, m=map(int, i.split())
    tot=0
    index=0
    while tot<m:
        tot+=n+index
        index+=1
    print(index)