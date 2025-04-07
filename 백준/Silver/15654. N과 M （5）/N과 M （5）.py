# collections 쓰지 않고 combination 구하기
N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
def func(arr):
    if(len(arr) == M):
        for i in arr:
            print(i,end=" ")
        print()
    else:
        for i in num:
            if(i not in arr):
                temp = arr[:]
                temp.append(i)
                func(temp)

for i in num:
    func([i])