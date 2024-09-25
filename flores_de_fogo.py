while True:
    try:
        r1, x1, y1, r2, x2, y2 = map(int, input().split())
        ct1 = abs(x1 - x2)
        ct2 = abs(y1 - y2)
        hyp = (ct1**2 + ct2**2)**0.5
        if r1 - r2 >= hyp:
            print("RICO")
        else:
            print("MORTO")

    except EOFError:
        break