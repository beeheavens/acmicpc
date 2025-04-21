h,m,s = map(int,input().split())
t = int(input())
h += (t//3600)
t = t % 3600
m += (t//60)
t = t % 60
s += t

m += s // 60
s = s % 60
h += m // 60
m = m % 60
print(f'{h%24} {m} {s}')