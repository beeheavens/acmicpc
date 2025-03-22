N = int(input())
data = []
for _ in range(N):
    pay, day = map(int,input().split())
    data.append([pay,day])
    
data.sort(key = lambda x: (-x[0],x[1]))
calender = [0 for i in range(10001)]

def find_day(d):
    for i in range(d-1,-1,-1):
        if(calender[i]==0):
            return i
    return -1

for i in data:
    pay = i[0]
    day = i[1]
    target = find_day(day)
    if(target != -1):
        calender[target] = pay

print(sum(calender))