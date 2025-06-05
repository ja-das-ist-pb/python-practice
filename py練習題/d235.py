while True:
    n=int(input())
    if n==0:
        break
    else:
        if n%11==0:
            print(n, "is a multiple of 11.")
        else:
            print(n, "is not a multiple of 11.")