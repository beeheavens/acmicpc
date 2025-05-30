# 처음부터 이야기의 진실을 아는 사람을 큐에 넣는다
# 그 사람들이 참가한 파티에서, 아직 진실을 몰랐던 사람들이 진실을 알게 될 것이고, 이 사람들을 다시 큐에 넣는다
# 결국 다 끝날때까지 과장 가능한 파티들이 몇개인지 구하면 된다
from collections import deque
N, M = map(int,input().split())
know_people = list(map(int,input().split()))
if len(know_people) == 1 : #아는 사람이 아무도 없는 경우
    know_people = []
else: # 아는 사람 수는 제거해도 됨
    del know_people[0] 


tf_party = [False for i in range(M)]
people_go = [[] for i in range(N)]
party = []
people_know = [False for i in range(N)]

for i in range(len(know_people)):
    know_people[i] -= 1
    people_know[know_people[i]] = True


for party_num in range(M):
    people = list(map(int,input().split()))
    for i in range(len(people)): # 리스트 안의 모든 값을 1 빼고 싶은데 어떻게 하지?
        people[i] -= 1
    del people[0]
    party.append(people)
    for person in people: # 이 사람이 이 파티에 갔다는 걸 저장
        people_go[person].append(party_num)

q = deque()
for p in know_people:
    q.append(p)
    
while(q):
    cur = q.popleft()
    for p in people_go[cur]: #그 사람이 갔던 파티들
        if(tf_party[p] == False):
            tf_party[p] = True
            for person in party[p]:
                if(people_know[person] == False):
                    people_know[person] = True
                    q.append(person)

print(tf_party.count(False))