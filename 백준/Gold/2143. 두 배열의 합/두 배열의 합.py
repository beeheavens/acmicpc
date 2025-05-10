from bisect import bisect_left,bisect_right

T = int(input())
a = int(input())
A = list(map(int,input().split()))
b = int(input())
B = list(map(int,input().split()))

def pref(arr):
    prefix_sum = [arr[0]]
    for i in range(1,len(arr)):
        prefix_sum.append(prefix_sum[i-1]+arr[i])
    ret = []
    for i in prefix_sum:
        ret.append(i)
    for i in range(len(prefix_sum)):
        for j in range(i+1,len(prefix_sum)):
            ret.append(prefix_sum[j]-prefix_sum[i])
    return ret

range_sum_A = pref(A)
range_sum_B = pref(B)
range_sum_B.sort()

ans = 0

for num in range_sum_A:
    target = T - num
    r = bisect_right(range_sum_B,target)
    l = bisect_left(range_sum_B,target)
    if(r==l):
        continue
    else:
        ans += r - l

print(ans)