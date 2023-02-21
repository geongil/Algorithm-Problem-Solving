import sys
from collections import deque
n = int(input())
q = deque([])
for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        q.append(a[1])
    elif a[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)
    elif a[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)

