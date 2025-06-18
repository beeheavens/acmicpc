def print_bottle(K):
    if K == 0:
        print("no more bottles",end = " ")
    elif K == 1:
        print("1 bottle",end = " ")
    else:
        print(f"{K} bottles",end = " ")

N = int(input())

for i in range(N,0,-1):
    print_bottle(i)
    print("of beer on the wall, ",end = "")
    print_bottle(i)
    print("of beer.")
    print("Take one down and pass it around, ",end="")
    print_bottle(i-1)
    print("of beer on the wall.")
    print()

print("No more bottles of beer on the wall, no more bottles of beer.")
print(f"Go to the store and buy some more, ",end="")
print_bottle(N)
print("of beer on the wall.")
