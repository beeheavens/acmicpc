import sys
sys.setrecursionlimit(1000000)

n, m = map(int,input().split())
parents = [i for i in range(n)] #자기 자신

def find(source):
    if parents[source] != source:
        return find(parents[source])
    return source

def union(x,y):
    rx = find(x)
    ry = find(y)
    if(rx != ry):
        parents[ry] = rx
        return False
    return True

ans = 0

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    if(union(a,b)):
        ans = _ + 1
        break

print(ans)