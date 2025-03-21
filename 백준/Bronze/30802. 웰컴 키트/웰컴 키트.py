N = int(input())
size = list(map(int,input().split()))
T, P = map(int,input().split())

total_T = 0
for i in size:
    total_T += i // T
    if(i%T >0):
        total_T += 1
print(total_T)
print(N//P,N%P)