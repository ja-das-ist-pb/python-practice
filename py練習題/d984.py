import sys

for i in sys.stdin:
    # aa=list(map(int, i.split()))
    # # a=[]
    # # a.append(("a", aa[0]))
    # # a.append(("b", aa[1]))
    # # a.append(("c", aa[2]))
    # a=list(zip(("A", "B", "C"), aa))
    a=[[x, y] for x, y in zip(("A", 'B', 'C'), list(map(int, i.split())))]
    a.sort(key=lambda x: (x[1], x[0]))
    last=a[0][1]
    a[0][1]=0
    a[1][1]+=last
    a.sort(key= lambda x: (x[1], x[0]))
    print(a[2][0])