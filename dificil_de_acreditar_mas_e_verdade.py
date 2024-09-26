while True:
    equacao = input()
    a = (equacao.split("+")[0])[::-1]
    b = ((equacao.split("+")[1]).split("=")[0])[::-1]
    c = (equacao.split("=")[1])[::-1]
    if equacao == "0+0=0":
        print(True)
        break
    if int(a) + int(b) == int(c):
        print(True)
    else:
        print(False)

