H,W = map(int,input().split()) #map size
blocks = list(map(int,input().split()))
main_map = [[0 for i in range(W)] for j in range(H)] # 맵 만들기

for idx,value in enumerate(blocks):
    for i in range(H-value,H):
        main_map[i][idx] = 1 #맵 생성


ans = 0

for i in range(H):
    flag = 0 
    visited = []
    for j in range(W):
        if(main_map[i][j] == 1 and flag == 0):
            flag = 1
        elif(main_map[i][j] == 0 and flag == 1):
            visited.append([i,j])
        elif(main_map[i][j] == 1 and flag == 1):
            ans += len(visited)
            for k in visited:
                main_map[k[0]][k[1]] = 2
            visited = []

print(ans)