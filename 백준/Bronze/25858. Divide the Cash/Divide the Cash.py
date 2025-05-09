t, m = map(int,input().split())
n = []
total = 0
for _ in range(t):
    temp = int(input())
    n.append(temp)
    total += temp
for i in n:
    print((m // total) * i)