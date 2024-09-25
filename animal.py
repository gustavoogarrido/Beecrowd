crt1 = input()
crt2 = input()
crt3 = input()
if crt1 == "vertebrado":
    if crt2 == "ave":
        if crt3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if crt3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if crt2 == "inseto":
        if crt3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if crt3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")