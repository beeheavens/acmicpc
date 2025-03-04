N = int(input())
for i in range(N):
    str = input()
    score = 0
    cur = 1
    for i in str:
        if(i == 'O'):
            score += cur
            cur += 1
        else:
            cur = 1
    print(score)