last = -1
while(1):
    num = float(input())
    if num == 999:
        break
    if last != -1:
        print(format(num-last,".2f"))
    last = num