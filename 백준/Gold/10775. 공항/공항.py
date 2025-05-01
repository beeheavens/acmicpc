import sys
sys.setrecursionlimit(10000000)
G = int(input())
P = int(input())
pointer = [i for i in range(G)]
airport = [0 for i in range(G)]
data = []

def find(target):
    if(pointer[target] != target):
        pointer[target] = find(pointer[target])
        return pointer[target]
    return pointer[target]

def union(target):
    if(target == 0 and airport[0] == 0):
        airport[0] = 1
        return True
    elif(target == 0 and airport[0] == 1):
        return False
    else:
        x = find(target-1)
        y = find(target)
        pointer[y] = x
        return True

for _ in range(P):
    data.append(int(sys.stdin.readline())-1)

ans = 0
for g in data:
    if(not union(find(g))):
        break
    ans += 1
print(ans)