while True:
    a=input()
    try:
        if isinstance(a, str):
            print(f'print("{a}")')
        else:
            print(f"print({a})")


    except a=="stop" or EOFError:
        break