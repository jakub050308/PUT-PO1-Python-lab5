n = int(input())
matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

currSum = 0
maxSum = 0

for i in range(n):
    for j in range(n):
        for i2 in range(i,n):
            for j2 in range(j,n):
                currSum = 0
                for r in range(i, i2+1):
                    for c in range(j, j2+1):
                        currSum += matrix[r][c]
                maxSum = max(currSum, maxSum)


print(maxSum)