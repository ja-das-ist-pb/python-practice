while True:
    try:
        n=int(input())
        if n%3==0:
            print("yes")
        else:
            print("no")
    except EOFError:
        break