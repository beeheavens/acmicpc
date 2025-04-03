T = int(input())

check = [[1,2,3],[4,5,6],[7,8,9]]

global up,down,left,right, front,back

up = [['w' for i in range(3)]for j in range(3)]
down = [['y' for i in range(3)]for j in range(3)]
left = [['g' for i in range(3)]for j in range(3)]
right = [['b' for i in range(3)]for j in range(3)]
front = [['r' for i in range(3)]for j in range(3)]
back = [['o' for i in range(3)]for j in range(3)]

def main_rotate(target,dir):
    next_view = [['t' for i in range(3)]for j in range(3)]
    if(dir == '-'): #반시계
        for i in range(3):
            for j in range(3):
                next_view[2-j][i] = target[i][j]
    elif(dir == '+'): #시계
        for i in range(3):
            for j in range(3):
                next_view[j][2-i] = target[i][j]
    return next_view
# 이차원 배열로 만들어 둔 큐브의 한 면은, 관찰을 어떻게 했을 때인가?

def check():
    for i in range(3):
        up[i][i] = 'kdfskl'

def left_func(dir):
    global up,down,left,right, front,back
    front_line = [front[0][0],front[1][0],front[2][0]]
    down_line = [down[0][0],down[1][0],down[2][0]]
    back_line = [back[2][2],back[1][2],back[0][2]]
    up_line = [up[0][0],up[1][0],up[2][0]]
    if(dir=='-'):
        for i in range(3):
            front[i][0] = down_line[i]
            down[i][0] = back_line[i]
            back[2-i][2] = up_line[i]
            up[i][0] = front_line[i]
    else:
        for i in range(3):
            front[i][0] = up_line[i]
            up[i][0] = back_line[i]
            back[2-i][2] = down_line[i]
            down[i][0] = front_line[i]
    

def right_func(dir):
    global up,down,left,right, front,back
    front_line = [front[0][2],front[1][2],front[2][2]]
    down_line = [down[0][2],down[1][2],down[2][2]]
    up_line = [up[0][2],up[1][2],up[2][2]]
    back_line = [back[2][0],back[1][0],back[0][0]]
    if(dir=='-'): # 반시계
        for i in range(3):
            front[i][2] = up_line[i]
            up[i][2] = back_line[i]
            back[2-i][0] = down_line[i]
            down[i][2] = front_line[i]
    else:
        for i in range(3):
            front[i][2] = down_line[i]
            down[i][2] = back_line[i]
            back[2-i][0] = up_line[i]
            up[i][2] = front_line[i]

def front_func(dir):

    global up,down,left,right, front,back
    up_line = [up[2][0],up[2][1],up[2][2]]
    right_line = [right[0][0],right[1][0],right[2][0]]
    down_line = [down[0][2],down[0][1],down[0][0]]
    left_line = [left[2][2],left[1][2],left[0][2]]
    if(dir == '-'): #반시계
        for i in range(3):
            up[2][i] = right_line[i]
            left[2-i][2] = up_line[i]
            down[0][2-i] = left_line[i]
            right[i][0] = down_line[i]
    else:
        for i in range(3):
            right[i][0] = up_line[i]
            up[2][i] = left_line[i]
            left[2-i][2] = down_line[i]
            down[0][2-i] = right_line[i]
    
def back_func(dir):

    global up,down,left,right, front,back
    up_line = [up[0][2],up[0][1],up[0][0]]
    left_line = [left[0][0],left[1][0],left[2][0]]
    down_line = [down[2][0],down[2][1],down[2][2]]
    right_line = [right[2][2],right[1][2],right[0][2]]
    if(dir=='-'): #반시계
        for i in range(3):
            up[0][2-i] = left_line[i]
            left[i][0] = down_line[i]
            down[2][i] = right_line[i]
            right[2-i][2] = up_line[i]
    else:
        for i in range(3):
            up[0][2-i] = right_line[i]
            right[2-i][2] = down_line[i]
            down[2][i] = left_line[i]
            left[i][0] = up_line[i]

def up_func(dir):
    global up,down,left,right, front,back
    left_line = [left[0][0],left[0][1],left[0][2]]
    front_line = [front[0][0],front[0][1],front[0][2]]
    right_line = [right[0][0],right[0][1],right[0][2]]
    back_line = [back[0][0],back[0][1],back[0][2]]
    if(dir == '-') :
        for i in range(3):
            front[0][i] = left_line[i]
            left[0][i] = back_line[i]
            back[0][i] = right_line[i]
            right[0][i] = front_line[i]
    else:
        for i in range(3):
            front[0][i] = right_line[i]
            right[0][i] = back_line[i]
            back[0][i] = left_line[i]
            left[0][i] = front_line[i]

def down_func(dir):

    global up,down,left,right, front,back
    left_line = [left[2][0],left[2][1],left[2][2]]
    front_line = [front[2][0],front[2][1],front[2][2]]
    right_line = [right[2][0],right[2][1],right[2][2]]
    back_line = [back[2][0],back[2][1],back[2][2]]
    if(dir == '-'):
        for i in range(3):
            front[2][i] = right_line[i]
            right[2][i] = back_line[i]
            back[2][i] = left_line[i]
            left[2][i] = front_line[i]
    else:
        for i in range(3):
            front[2][i] = left_line[i]
            left[2][i] = back_line[i]
            back[2][i] = right_line[i]
            right[2][i] = front_line[i]

## main

for _ in range(T):
    n = int(input())
    op = list(map(str,input().split())) #operations

    up = [['w' for i in range(3)]for j in range(3)]
    down = [['y' for i in range(3)]for j in range(3)]
    left = [['g' for i in range(3)]for j in range(3)]
    right = [['b' for i in range(3)]for j in range(3)]
    front = [['r' for i in range(3)]for j in range(3)]
    back = [['o' for i in range(3)]for j in range(3)]

    for i in op:
        target = i[0]
        direction = i[1]
        if(target == 'L'):
            left_func(direction)
            left = main_rotate(left,direction)
        elif(target == 'R'):
            right_func(direction)
            right = main_rotate(right,direction)
        elif(target == 'U'):
            up_func(direction)
            up = main_rotate(up,direction)
        elif(target == 'D'):
            down_func(direction)
            down = main_rotate(down,direction)
        elif(target == 'F'):
            front_func(direction)
            front = main_rotate(front,direction)
        elif(target == 'B'):
            back_func(direction)
            back = main_rotate(back,direction)
    for i in up:
        line = ''
        for j in i:
            line += j
        print(line)
