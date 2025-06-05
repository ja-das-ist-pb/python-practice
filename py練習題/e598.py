from math import *

a=input()
length=len(a)
numa=int(a)
isgood=True

for i in range(10**8, numa):
    if numa%i==0:
        isgood=False
        break
if not isgood:
    print("no")
else: print("yes")