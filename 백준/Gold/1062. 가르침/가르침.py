import sys
import itertools
# anta # tica 
# a n t i c 이 없으면, 한 단어도 읽을 수 없다.
# 최소 5개는 읽을 수 있어야 한다. 

input = sys.stdin.readline 
N, K = map(int, input().strip().split())

def sol(n, k):
  # 초기 셋팅
  uniqueList = []
  uniqueSet = set()
  cnt = 0
  # N개의 단어 읽기
  for _ in range(n):
    now = input().strip()
    nowset = set(now)
    nowcnt = len(nowset)
    # 읽을 수 없는 경우
    if nowcnt > k:
      continue
    # 무조건 읽는 경우
    if nowcnt == 5:
      cnt += 1
      continue
    # 6개 이상 K개 이하인 경우
    nowunique = nowset - {'a','n','t','i','c'}
    uniqueList.append(nowunique)
    uniqueSet = uniqueSet.union(nowunique)

  # K가 5보다 작으면, 단 하나의 단어도 읽을 수 없음
  if k < 5:
    return 0 
    
  # K는 5보다 크거나 같은데, 주어진 words는 모두 a,n,t,i,c 5개 알파벳으로만 이루어진 경우
  if len(uniqueList) == 0:
    return cnt
    
  # antic 외에 K-5개 이하로 알파벳을 사용해도 모든 단어를 다 읽을 수 있는 경우
  if len(uniqueSet) <= k-5 :
    return cnt + len(uniqueList)

  # K-5개의 알파벳을 어떤 조합으로 골라야 가장 많이 읽을 수 있나 Brute-Force
  maxCnt = 0
  
  for case in itertools.combinations(uniqueSet, k-5):
    caseCnt = 0
    caseSet = set(case)
    for candidateSet in uniqueList:
      if candidateSet.issubset(caseSet):
        caseCnt += 1
    maxCnt = max(maxCnt, caseCnt)

  # 최종적으로 얻어낸 cnt를 얻어서 반환해주기
    
  cnt += maxCnt
  return cnt
  
print(sol(N, K))