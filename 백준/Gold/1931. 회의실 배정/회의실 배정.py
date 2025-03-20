N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int,input().split())))

data.sort(key=  lambda x : (x[1],x[0])) # x[1]을 기준으로 정렬

ans = 0
last = -1
for i in data:
    if(i[0] >= last):
        ans += 1
        last = i[1]

print(ans)