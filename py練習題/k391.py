import sys
def input(): return sys.stdin.readline().strip()

s, sn=map(str, input().split())
o, on=map(str, input().split())
sn=int(sn)
on=int(on)
if sn==on:
    print('tie')
elif sn>on:
    print(s, "WIN!")
elif sn<on:
    print(o, "WIN!")