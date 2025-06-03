total = int(input())
a = int(input())
for _ in range(a):
    cost, quantity = map(int,input().split())
    total -= cost*quantity
   
if total == 0:
    print('Yes')
else:
    print('No')