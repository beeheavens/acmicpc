# BF로 해보자
# from itertools import permutations
# N = int(input())
# temp = [i for i in range(N)]
# perm = list(permutations(temp,N))
# print(len(perm))

# N = int(input())
# global ans
# ans = 0


# def sol(queens,row):
#     global ans
#     for col in range(N):
#         flag = 0
#         for q in queens:
#             if(q[1] == col): #이미 같은 x값에 퀸이 존재
#                 flag = 1
#                 break
#             if(abs(q[0]-row)==abs(q[1]-col)):
#                 flag = 1
#                 break
#         if(flag == 0): #문제없었다면
#             if(row == N-1):
#                 ans += 1
#             else:
#                 next = []
#                 for i in queens:
#                     next.append(i)
#                 next.append([row,col])
#                 sol(next,row+1)

# sol([],0)
# print(ans)

N = int(input())
global ans
ans = 0

used_col = [0 for i in range(N)]
used_yx = [0 for i in range(2*N -1)]
used_yx2 = [0 for i in range(2*N - 1)]

def sol(row, u_c, u_yx, u_yx2):
    global ans
    for col in range(N):
        if(u_c[col] == 1):
            continue
        local_yx = row+col
        if(u_yx[local_yx] == 1):
            continue
        local_yx2 = N - 1 - row + col
        if(u_yx2[local_yx2] == 1):
            continue
        if(row == N-1):
            ans += 1
        else:
            temp0 = u_c[:]
            temp0[col] = 1
            temp1 = u_yx[:]
            temp1[local_yx] = 1
            temp2 = u_yx2[:]
            temp2[local_yx2] = 1
            sol(row+1, temp0, temp1,temp2)

sol(0,used_col,used_yx,used_yx2)
print(ans)
        