# L1 = t1 * x + a
# L2 = t2 * x + b
# 연립 후 나온 해가 범위 안에 속하는지 계산
# 평행하면 어떡하지? 이거 생각해야겠다.

x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())

if(x2==x1 and x3==x4): # 둘 다 세로로 평행
    if(x1 == x3):
        if(min(y1,y2)<=min(y3,y4)<=max(y1,y2) or min(y1,y2)<=max(y3,y4)<=max(y1,y2)):
            print(1)
        elif(min(y3,y4)<=min(y1,y2)<=max(y3,y4) or min(y3,y4)<=max(y1,y2)<=max(y3,y4)):
            print(1)
        else:
            print(0)
    else:
        print(0)
elif(x2 == x1 and x3 != x4): # 하나만 세로로 수직이면
    t2 = (y4-y3) / (x4-x3) # 기울기 2
    b = y3 - t2*x3
    target = t2 * x1 + b
    if(min(x3,x4) <= x1 <= max(x3,x4)):        
        if(min(y1,y2) <= target <= max(y1,y2)):
            print(1)
        else:
            print(0)
    else:
        print(0)
elif(x3 == x4 and x1 != x2):
    t1 = (y2-y1) / (x2-x1) # 기울기 1
    t1 = round(t1,9)
    a = y1 - t1 * x1
    target = t1 * x3 + a
    if(min(x1,x2)<= x3 <= max(x1,x2)):
        if(min(y3,y4) <= target<= max(y3,y4)):
            print(1)
        else:
            print(0)
    else:
        print(0)
else:
    t1 = (y2-y1) / (x2-x1) # 기울기 1
    t2 = (y4-y3) / (x4-x3) # 기울기 2
    t1 = round(t1,9)
    t2 = round(t2,9)

    if(t1 != t2): #평행하지 않은 경우
        a = y1 - t1*x1
        b = y3 - t2*x3
        sol = (b-a) / (t1-t2)
        sol = round(sol)
        if(min(x1,x2) <= sol <= max(x1,x2) and min(x3,x4) <= sol <= max(x3,x4)):
            print(1)
        else:
            print(0)
    elif(t1 == t2): # 두 직선이 평행한 경우
        #절편을 구하자
        a = y1 - t1*x1
        b = y3 - t2*x3
        if(a != b): # 절편이 다르면 절대 못만남
            print(0)
        else: # 절편이 같으면 범위가 겹치는지 확인해야함
            if(min(x3,x4)<=min(x1,x2)<=max(x3,x4) or min(x3,x4)<= max(x1,x2)<=max(x3,x4)):
                print(1)
            elif(min(x1,x2)<=min(x3,x4)<=max(x1,x2) or min(x1,x2)<= max(x3,x4)<=max(x1,x2)):
                print(1)
            else:
                print(0)
