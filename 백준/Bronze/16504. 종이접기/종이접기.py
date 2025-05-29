a = int(input())
data = []
for _ in range(a):
    data.append(list(map(int,input().split())))


ans = 0
for i in data:
    ans += sum(i)

print(ans)