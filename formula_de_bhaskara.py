a, b, c = map(float, input().split())
delta = b**2 - 4 * a * c
if delta >= 0:
    if a != 0:
        r1 = (-b + delta**0.5)/(2*a)
        r2 = (-b - delta**0.5)/(2*a)
        print(f"R1 = {round(r1, 5)}\nR2 = {round(r2, 5)}")
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")