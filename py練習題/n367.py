import math

a, b, c=map(int, input())
st=[]*3
st[0]=math.sqrt(a)
st[1]=math.sqrt(b)
st[2]=math.sqrt(c)

if st[0]+st[1]<st[2] or st[1]+st[2]<st[0] or st[0]+st[2]<st[1]:
    print("error")
else:
    s=sum(st)/2
    print(f"{st[0]:.4f}")
    print(f"{st[1]:.4f}")
    print(f"{st[2]:.4f}")
    print(f"{math.sqrt(s*(s-st[0])*(s-st[1])*(s-st[2])):.4f}")