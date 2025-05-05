import sys
N = int(input())
A = []
B = []
C = []
D = []

for _ in range(N):
    a,b,c,d = map(int,sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

a = {}
b = []
for t_a in A:
    for t_b in B:
        target = t_a + t_b
        if(target in a):
            a[target] += 1
        else:
            a[target] = 1

for t_c in C:
    for t_d in D:
        b.append(t_c+t_d)

ans = 0
for i in b:
    if(i*-1 in a):
       ans += a[i*-1]

print(ans) 

