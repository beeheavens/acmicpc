A = int(input())
B = int(input())
C = int(input())

ans = A * B * C
str = str(ans)
nums = [0 for i in range (10)]
for i in str:
    nums[int(i)] += 1

for i in nums:
    print(i)