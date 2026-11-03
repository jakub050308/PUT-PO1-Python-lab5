n = int(input())
a = [int(x) for x in input().split()]

a = sorted(a)

for i in a:
    print(i, end=" ")

