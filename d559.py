while True:
    try:
        n=input()
        s="'C' can use printf(" + '"%d",n); to show integer like ' + n
        print(s)
    except EOFError:
        break