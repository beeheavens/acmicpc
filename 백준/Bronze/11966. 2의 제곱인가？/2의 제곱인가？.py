a = int(input())
start = 2
flag = 0
if(a == 1 or a == 2):
    print(1)
    flag = 1
while(start < a):
    start *= 2
    if(start == a):
        print(1)
        flag = 1

if flag == 0:
    print(0)