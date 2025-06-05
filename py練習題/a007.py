import math

while True:
    try:
        n=int(input())
        p=True
        for i in range(2, int(math.sqrt(n))+2):
            if n%i==0:
                print("非質數")
                p=False
                break
        if p: print("質數")
    except EOFError:
        break
        