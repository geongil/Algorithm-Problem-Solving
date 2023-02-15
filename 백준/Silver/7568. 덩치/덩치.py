N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

k_arr = [1 for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if (arr[i][0] < arr[j][0]) and (arr[i][1] < arr[j][1]):
            k_arr[i] += 1

        elif (arr[i][0] > arr[j][0]) and (arr[i][1] > arr[j][1]):
            k_arr[j] += 1

for i in k_arr:
    print(i, end=" ")
