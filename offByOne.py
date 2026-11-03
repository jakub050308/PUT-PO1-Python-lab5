def search(d, table):
    val = False
    for t in range(d-1):
        if abs(table[t] - table[t+1]) == 1:
            val = True
    return val


n = int(input())
nums = [int(x) for x in input().split()]

if search(n, nums):
    print("YES")
else:
    print("NO")