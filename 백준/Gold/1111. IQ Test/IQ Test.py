N = int(input())
num = list(map(int,input().split()))

#ax + b
if(N == 1):
    print('A')
elif N == 2:
    if num[0] == num[1]:
        print(num[0])
    else:
        print('A')
else:
    if(num[1] == num[0]):
        a = 1
        b = 0
    else:
        a = (num[2] - num[1]) // (num[1] - num[0])
        b = num[1] - (num[0]*a)
    flag = 0
    for i in range(1,N):
        if num[i] != num[i-1]*a + b:
            flag = 1
            break
    if flag == 1:
        print('B')
    else:
        print(num[N-1]*a + b)