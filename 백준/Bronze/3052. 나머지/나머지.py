num = []
for i in range(10):
    num.append(int(input())%42)

numset = set(num)
print(len(numset))