#일단 뒤집어?
def convert(map,start):
    cur_y = start[0]
    cur_x = start[1]
    for i in range(3):
        for j in range(3):
            map[cur_y+i][cur_x + j] = (map[cur_y+i][cur_x + j]+1)%2

N,M = map(int,input().split())
A = []
B = []
for _ in range(N):
    temp = []
    a = input()
    for i in a:
        temp.append(int(i))
    A.append(temp)
for _ in range(N):
    temp = []
    a = input()
    for i in a:
        temp.append(int(i))
    B.append(temp)
ans = 0


if(N < 3 or M < 3):
    flag = 0
    for i in range(N):
        for j in range(M):
            if(A[i][j] != B[i][j]):
                flag = 1
    if(flag == 0):
        print(0)
    else:
        print(-1)

else:
    flag = 0
    for i in range(N-2):
        for j in range(M-2):
            if(A[i][j]!=B[i][j]):
                convert(A,[i,j])
                ans += 1
        for j in range(M-2,M):
            if(A[i][j]!=B[i][j]):
                print(-1)
                flag = 1
                break
        if(flag==1):
            break
    if(flag == 0):
        for i in range(N-2,N):
            for j in range(M):
                if(A[i][j]!=B[i][j]):
                    flag = 1
                    print(-1)
                    break
            if(flag == 1):
                break
    if(flag == 0):
        print(ans)
        

                
