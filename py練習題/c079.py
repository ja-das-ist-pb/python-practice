while True:
    try:
        n, k=map(int, input().split())
        tot=n
        a=n
        while a>=k:
            tot+=a//k
            a=a//k+a%k
        print(tot)
    except EOFError:
        break