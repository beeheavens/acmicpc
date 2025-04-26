T = int(input())

for testcase in range(T):
    student = int(input())
    select = list(map(int, input().split()))
    
    # 1부터 시작하는 입력을 0부터 시작하는 인덱스로 변환
    for i in range(student):
        select[i] -= 1
    
    visited = [0] * student
    ans = 0  # 사이클에 포함된 학생 수
    
    for i in range(student):
        if visited[i] == 1:
            continue
        
        # 현재 경로를 추적하기 위한 집합
        path = set()
        cur = i
        
        # DFS로 사이클 찾기
        while visited[cur] == 0:
            visited[cur] = 1
            path.add(cur)
            cur = select[cur]
            
            # 사이클 발견
            if cur in path:
                # 사이클의 시작점 찾기
                cycle_start = cur
                cycle_count = 1
                next_student = select[cur]
                
                # 사이클의 크기 계산
                while next_student != cycle_start:
                    cycle_count += 1
                    next_student = select[next_student]
                
                ans += cycle_count
                break
            
            # 이미 방문한 노드를 만난 경우 (다른 사이클에 연결됨)
            if visited[cur] == 1 and cur not in path:
                break
    
    print(student - ans)