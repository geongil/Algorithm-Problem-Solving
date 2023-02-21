n, k = map(int, input().split())

q = []
result = []
cnt = 0

for i in range(1, n + 1):
    q.append(i)

# 1 2 3 4 5 6 7     4 5 6 7 1 2
while True:
    if len(q) == 0:
        a = ', '.join(result)
        print(f'<{a}>')
        break
    if cnt == (k - 1):
        result.append(str(q.pop(0)))
        cnt = 0
    else:
        q.append(q.pop(0))
        cnt += 1
