while True:
    try:
        a, b, c, d, e, f=map(int, input().split())
        
        d=a*e-b*d
        dx=c*e-b*f
        dy=a*f-c*d

        if d!=0:
            x=dx/d
            y=dy/d
            print(f"x={x:.2f}")
            print(f"y={y:.2f}")
        else:
            if dx==0 and dy==0:
                print("Too many")
            else:
                print("No answer")

    except:
        break