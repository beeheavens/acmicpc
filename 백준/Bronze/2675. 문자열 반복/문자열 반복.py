N = int(input())
for i in range(N):
    rep, str = input().split()
    temp = ''
    for j in str:
        for k in range(int(rep)):
            temp += j
    print(temp)
