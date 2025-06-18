N, M, K = map(int,input().split()) # 세로, 가로, 스티커 수
stickers = []
for _ in range(K):
    data =[]
    R, C = map(int,input().split())
    for _ in range(R):
        data.append(list(map(int,input().split())))
    stickers.append(data)

notebook = [[0 for i in range(M)]for j in range(N)]

#기준점(좌측 최상단)으로 시작해서, 스티커의 크기만큼 비교하는 함수
#스티커를 붙일 수 있으면 True를 반환
def stick_check(source, sticker):
    y_len = len(sticker) # 스티커의 y 길이
    x_len = len(sticker[0]) # 스티커의 x 길이
    source_y = source[0]
    source_x = source[1]
    flag = 0
    for i in range(y_len):
        for j in range(x_len):
            if(sticker[i][j] == 1 and notebook[source_y+i][source_x+j] == 1):
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        return True
    else:
        return False

#스티커를 붙이는 함수
def stick(source,sticker):
    y_len = len(sticker)
    x_len = len(sticker[0])
    source_y = source[0]
    source_x = source[1]
    for i in range(y_len):
        for j in range(x_len):
            if(sticker[i][j]==1):
                notebook[source_y+i][source_x+j] = 1

#시계 방향으로 90도 회전시킨 스티커를 반환
def rotate(sticker):
    ret = []
    for i in range(len(sticker[0])):
        temp = []
        for j in range(len(sticker)-1,-1,-1):
            temp.append(sticker[j][i])
        ret.append(temp)
    return ret

for sticker in stickers:
    flag = 0
    for d in range(4):
        y_len = len(sticker)
        x_len = len(sticker[0])
        for i in range(N-y_len+1):
            for j in range(M-x_len+1):
                if stick_check([i,j],sticker):
                    stick([i,j],sticker)
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 1:
            break
        else:
            sticker = rotate(sticker)

ans = 0 
for i in range(N):
    for j in range(M):
        if notebook[i][j]==1:
            ans += 1

print(ans)