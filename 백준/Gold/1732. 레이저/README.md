# [Gold II] 레이저 - 1732 

[문제 링크](https://www.acmicpc.net/problem/1732) 

### 성능 요약

메모리: 146648 KB, 시간: 292 ms

### 분류

기하학, 정렬

### 제출 일자

2025년 6월 18일 17:33:40

### 문제 설명

<p>2차원 평면상에 N(1≤N≤100,000)개의 기둥이 설치되어 있다. 각각의 기둥의 꼭대기에는 레이저가 설치되어 있는데, 레이저는 (0, 0)의 위치에 있는 조각상을 비추고 있다. 각각의 건물의 높이는 다를 수 있는데, 이때문에 몇몇 레이저들은 다른 건물에 가려질 수도 있다. 두 개의 건물 A, B와 조각상이 일직선상에 순서대로 있을 때, 만약 A의 높이가 B의 높이 이하이면 A의 꼭대기에 설치되어 있는 레이저는 건물 B에 가려지게 된다.</p>
<p>각 건물들의 좌표가 주어졌을 때, 레이저가 가려지게 되는 건물들을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다. 다음 N개의 줄에는 세 정수 x, y, z가 주어진다. 이는 (x, y)의 위치에 높이 z인 건물이 존재한다는 의미이다. 단 -100,000≤x≤100,000, 0≤y≤10,000, 0≤z≤10,000이 만족된다. 같은 위치에는 최대 한 개의 건물만 있을 수 있다.</p>

### 출력 

 <p>첫째 줄부터 가려지는 건물들의 좌표를 출력한다. 좌표를 출력할 때에는 x좌표가 증가하는 순서대로, x좌표가 같다면 y좌표가 증가하는 순서대로 출력한다.</p>

