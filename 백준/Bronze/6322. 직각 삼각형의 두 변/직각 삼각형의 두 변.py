case = 1
while True :
    a, b, c = map(int, input().split())
    if a == b == c == 0 : break
    print(f"Triangle #{case}")
    if a == -1 :
        if c ** 2 - b ** 2 > 0 : print("a = {:.3f}".format((c ** 2 - b ** 2) ** 0.5))
        else : print("Impossible.")
    if b == -1 :
        if c ** 2 - a ** 2 > 0 : print("b = {:.3f}".format((c ** 2 - a ** 2) ** 0.5))
        else : print("Impossible.")
    if c == -1 :
        if a ** 2 + b ** 2 > 0 : print("c = {:.3f}".format((a ** 2 + b ** 2) ** 0.5))
        else : print("Impossible.")
    print()
    case += 1