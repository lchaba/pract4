print("введите количество элементов: ")
n = int(input())
print("введите список: ")
l = list(map(int,input().split()))

for a in range (n-1):
    for i in range(n-1-a):
        if l[i]>l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
print("получившийся список: ")
print(l)