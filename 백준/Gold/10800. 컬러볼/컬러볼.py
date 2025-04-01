import sys
N = int(input())

color_dict = {}
size_dict = {}
data =[]
ans = [0 for i in range(N)]
for _ in range(N):
    temp = (list(map(int,sys.stdin.readline().split())))
    temp.append(_)
    data.append(temp)

data.sort(key = lambda x : (x[1],x[0]))
for ball in data:
    color, size, position = ball
    if(size in size_dict):
        size_dict[size].append(ball)
    else:
        size_dict[size] = [ball]

max_size = data[len(data)-1][1] # 제일 큰 놈


sum = 0
for i in range(max_size+1):
    if(i in size_dict):
        temp_sum = 0
        temp = []
        for ball in size_dict[i]:
            color, size, position = ball
            if(color in color_dict):
                ans[position] = sum - color_dict[color]
            else:
                ans[position] = sum
            temp_sum += size
            temp.append(ball)
        for t in temp:
            color, size, position = t
            if(color in color_dict):
                color_dict[color] += size
            else:
                color_dict[color] = size
        sum += temp_sum

for i in ans:
    print(i)