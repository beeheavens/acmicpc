birth = input()
n = int(input())
max = 0
ans = "99999999"
for _ in range(n):
    target = input()
    y = 0
    m = 0
    d = 0
    for i in range(4):
        y += (int(birth[i]) - int(target[i]))**2
    for i in range(4,6):
        m += (int(birth[i])- int(target[i]))**2
    for i in range(6,8):
        d += (int(birth[i])- int(target[i]))**2
    bio = y*m*d
    if(max < bio):
        max = bio
        ans = target
    if(max == bio):
        if(int(ans) > int(target)):
            ans = target

print(ans)