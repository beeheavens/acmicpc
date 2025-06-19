T = int(input())
for _ in range(T):
    M = int(input())
    ratio = 0
    ans = 0
    for i in range(M):
        g, w = map(int,input().split())
        temp_r = g / w
        if(temp_r > ratio):
            ratio = temp_r
            ans = w
        elif temp_r == ratio:
            if ans > w:
                ans = w
    print(ans)