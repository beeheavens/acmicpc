N, K = map(int,input().split())
map = [-1] * 100001

map[N] = 0
new = [N]
while(map[K] == -1):
    next_new = []
    for i in new:
        next = i*2 # 순간이동
        if(0<= next <= 100000):
            if(map[next] == -1 or map[next] > map[i]):
                map[next] = map[i]
                next_new.append(next)
        next = i+1
        if(0<= next <= 100000):
            if(map[next] == -1 or map[next] > map[i]):
                map[next] = map[i] + 1
                next_new.append(next)
        next = i-1
        if(0<= next <= 100000):
            if(map[next] == -1 or map[next] > map[i]):
                map[next] = map[i] + 1
                next_new.append(next)
    new = next_new

print(map[K])
         