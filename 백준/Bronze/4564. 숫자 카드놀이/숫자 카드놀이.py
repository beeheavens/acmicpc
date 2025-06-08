while(1):
    num = input()
    if(num == '0'):
        break
    while(len(num)>1):
        print(num,end=" ")
        next = 1
        for i in num:
            next *= int(i)
        num = str(next)
    print(num)