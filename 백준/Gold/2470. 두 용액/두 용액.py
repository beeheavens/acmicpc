N = int(input())
num = list(map(int,input().split()))
num.sort()

ans_start = 0
ans_end = len(num)-1
sum = abs(num[ans_start] + num[ans_end])

start = 0
end = len(num)-1
while(start!=end):
    temp_sum = (num[start] + num[end])
    if(sum > abs(temp_sum)):
        ans_start = start
        ans_end = end
        sum = abs(temp_sum)
        if(temp_sum == 0):
            break
    if(temp_sum > 0):
        end -= 1
    else:
        start += 1

print(num[ans_start], num[ans_end])