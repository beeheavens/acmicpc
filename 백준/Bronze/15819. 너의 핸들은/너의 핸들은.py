N, target = map(int,input().split())
data = []
for _ in range(N):
    data.append(input())

data.sort()
print(data[target-1])
