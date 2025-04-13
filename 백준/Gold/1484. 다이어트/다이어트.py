G = int(input())
a = 2
b = 1
ans = []
while(b<a):
    diff= a**2 - b**2
    if(diff > G):
        b += 1
    elif(diff < G):
        a += 1
    elif(diff==G):
        ans.append(a)
        a += 1
        b += 1
if(len(ans)==0):
    print(-1)
else:
    for i in ans:
        print(i)