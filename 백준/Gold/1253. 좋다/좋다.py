N = int(input())
num = list(map(int,input().split()))
num.sort()

def isgood(target,arr):
    start = 0
    end = len(arr) - 1
    while(start != end):
        calc = arr[start] + arr[end]
        if(calc == target):
            return True
        if(calc > target):
            end -= 1
        else:
            start += 1
    return False

ans = 0
for idx,value in enumerate(num):
    temp = num[:]
    del temp[idx]
    if(isgood(value,temp)):
        ans += 1

print(ans)    