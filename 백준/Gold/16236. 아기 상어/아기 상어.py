import sys
from collections import deque
import copy

global shark, shark_eat, shark_size
N = int(input())
space = []
for _ in range(N):
    space.append(list(map(int, sys.stdin.readline().split())))

shark = []  # 위치
shark_eat = 0  # 먹은 물고기
shark_size = 2  # 크기

dy = [-1, 0, 0, 1]  # 상, 좌, 우, 하 (우선순위 고려하여 변경)
dx = [0, -1, 1, 0]

# 상어 초기 위치 찾기
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark = [i, j]  # 상어 초기 위치
            space[i][j] = 0  # 상어 위치를 0으로 변경

def bfs():
    global shark, shark_eat, shark_size
    
    # 방문 배열 초기화
    visited = [[-1] * N for _ in range(N)]
    visited[shark[0]][shark[1]] = 0
    
    queue = deque([shark])
    
    # 먹을 수 있는 물고기 후보들
    candidates = []
    
    while queue:
        y, x = queue.popleft()
        
        # 만약 이미 물고기를 찾았고, 현재 거리가 그 물고기보다 멀다면 더 이상 탐색할 필요 없음
        if candidates and visited[y][x] > candidates[0][2]:
            break
            
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            # 맵 범위 내이고 방문하지 않았으며, 상어 크기보다 작거나 같은 칸만 이동 가능
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1 and space[ny][nx] <= shark_size:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))
                
                # 먹을 수 있는 물고기 발견 (0보다 크고 상어 크기보다 작은 물고기)
                if 0 < space[ny][nx] < shark_size:
                    candidates.append((ny, nx, visited[ny][nx]))
    
    # 먹을 수 있는 물고기가 없다면
    if not candidates:
        return None
        
    # 거리, y좌표, x좌표 순으로 정렬 (문제 조건에 맞게)
    candidates.sort(key=lambda x: (x[2], x[0], x[1]))
    
    # 가장 우선순위가 높은 물고기 선택
    return candidates[0]

def simulate():
    global shark, shark_eat, shark_size
    
    total_time = 0
    
    while True:
        # BFS로 먹을 물고기 찾기
        result = bfs()
        
        # 더 이상 먹을 물고기가 없으면 종료
        if result is None:
            break
            
        # 물고기 위치로 상어 이동
        shark = [result[0], result[1]]
        
        # 총 이동 시간 누적
        total_time += result[2]
        
        # 물고기 제거
        space[result[0]][result[1]] = 0
        
        # 먹은 물고기 수 증가
        shark_eat += 1
        
        # 상어 크기만큼 물고기를 먹었으면 크기 증가
        if shark_eat == shark_size:
            shark_size += 1
            shark_eat = 0
            
    return total_time

print(simulate())