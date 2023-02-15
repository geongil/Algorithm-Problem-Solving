N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

mat = [[0 for _ in range(101)] for _ in range(101)]
cnt = 0
for i in range(N):
    for j in range(arr[i][0] + 9, arr[i][0] - 1, -1):
        for k in range(arr[i][1] + 9, arr[i][1] - 1, -1):
            mat[j][k] += 1

for i in range(100):
    for j in range(100):
        if mat[i][j] >= 1:
            cnt += 1

print(cnt)

