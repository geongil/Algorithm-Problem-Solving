def dfs(num):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    else:
        for i in range(num, n + 1):
            if not visited[i]:
                visited[i] = 1
                result.append(i)
                dfs(i + 1)
                visited[i] = 0
                result.pop()


n, m = map(int, input().split())
visited = [0] * (n + 1)
result = []
dfs(1)
