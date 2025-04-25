N = int(input())
global min
nums = list(map(int,input().split()))
nums.sort()
ans = []
min = float("inf")

def sol(target):
    global min
    ret = []
    start = 0
    end = len(nums)-1
    t = nums[target]
    while(start < target and target < end):
        calc = nums[start] + t + nums[end]
        if(abs(calc) < min):
            min = abs(calc)
            ret = [nums[start],t,nums[end]]
            if(calc > 0):
                end -= 1
            else:
                start += 1
        else:
            if(calc > 0):
                end -= 1
            else:
                start += 1
    return ret

for i in range(1,N-1):
    result = sol(i)
    if(len(result)==3):
        ans = result

for i in ans:
    print(i,end = " ")