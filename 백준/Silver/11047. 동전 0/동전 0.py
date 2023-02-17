n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.reverse()
result = 0

for i in range(n):
    if arr[i] <= k:
        money = k // arr[i]
        k = k - (arr[i] * money)
        result += money

    if k == 0:
        break

print(result)
