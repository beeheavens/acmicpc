import sys

S = set()

num = int(input())
for i in range(num):
    temp = sys.stdin.readline().strip().split()
    if(len(temp)==1):
        cmd = temp[0]
        if(cmd == 'all'):
            S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        elif(cmd == 'empty'):
            S = set()
    
    else:
        cmd , n = temp[0],temp[1]
        n = int(n)
        if(cmd == 'add'):
            S.add(n)
        elif(cmd == 'remove'):
            S.discard(n)
        elif(cmd == 'check'):
            if(n in S):
                print(1)
            else:
                print(0)
        elif(cmd == 'toggle'):
            if(n in S):
                S.discard(n)
            else:
                S.add(n)
    
