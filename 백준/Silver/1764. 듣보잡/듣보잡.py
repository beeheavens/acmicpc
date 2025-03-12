D = set()
DB = set()
d,b = input().split()
d = int(d)
b = int(b)
for _ in range(d):
    D.add(input())

for _ in range(b):
    person = input()
    if(person in D):
        DB.add(person)

DB = sorted(DB)
print(len(DB))
for i in DB:
    print(i)