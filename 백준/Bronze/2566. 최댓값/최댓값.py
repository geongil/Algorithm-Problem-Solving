arr = [list(map(int, input().split())) for _ in range(9)]

mx = 0
mi = 0
mj = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] >= mx:
            mx = arr[i][j]
            mi = i + 1
            mj = j + 1

print(mx)
print(mi, mj)
