def dfs(num):
    if num == m:
        print(" ".join(map(str, result)))
        return
    else:
        for i in range(1, n + 1):
            if not visited[i]:
                visited[i] = 1
                result.append(i)
                dfs(num + 1)
                visited[i] = 0
                result.pop()


n, m = map(int, input().split())
result = []
visited = [0] * (n + 1)
dfs(0)
