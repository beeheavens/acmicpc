max = 0
max_line = 0
for i in range(9):
    target = int(input())
    if(target > max):
        max = target
        max_line = i+1

print(max)
print(max_line)