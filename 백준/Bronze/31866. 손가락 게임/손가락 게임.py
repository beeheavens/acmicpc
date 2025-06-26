a, b = map(int,input().split())
if a == 0:
    if b == 0:
        print('=')
    elif b == 2:
        print('>')
    elif b == 5:
        print('<')
    else:
        print('>')
elif a == 2:
    if b == 0:
        print('<')
    elif b == 2:
        print('=')
    elif b == 5:
        print('>')
    else:
        print('>')
elif a == 5:
    if b == 0:
        print('>')
    elif b == 2:
        print('<')
    elif b == 5:
        print('=')
    else:
        print('>')
else:
    if b == 0 or b == 2 or b == 5:
        print('<')
    else:
        print('=')