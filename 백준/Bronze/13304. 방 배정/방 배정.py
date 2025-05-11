import math
N, K = map(int,input().split())

a = 0
b = 0
c = 0
d = 0 
e = 0

for _ in range(N):
    s, age = map(int,input().split())
    if(age == 1 or age == 2):
        a += 1
    elif(age == 3 or age == 4):
        if(s == 0):
            b += 1
        elif s == 1:
            c += 1
    elif(age == 5 or age == 6):
        if(s == 0):
            d += 1
        elif s == 1:
            e += 1

ans = 0
ans += math.ceil(a/K)
ans += math.ceil(b/K) 
ans += math.ceil(c/K) 
ans += math.ceil(d/K) 
ans += math.ceil(e/K) 
print(ans)