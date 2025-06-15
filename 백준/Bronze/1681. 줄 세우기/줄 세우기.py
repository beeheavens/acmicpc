ans = 1
N, L = map(int,input().split())
while(N>0):
    if str(L) in str(ans):
        ans += 1
    else:
        N -= 1
        ans += 1

print(ans-1)