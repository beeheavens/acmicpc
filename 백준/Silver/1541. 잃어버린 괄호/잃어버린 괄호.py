## 1. '-' 뒤의 '+'을 전부 괄호로 묶자

equation = input()
temp = equation.split('-')
values = []
for i in temp:
    i = list(map(int,i.split('+')))
    values.append(sum(i))

target = values[0]
del values[0]
for i in values:
    target -= i
print(target)