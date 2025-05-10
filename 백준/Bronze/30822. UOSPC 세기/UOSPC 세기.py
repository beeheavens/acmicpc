n = int(input())
string = input()

c = [string.count(i) for i in "uospc"]
print(min(c))