n = int(input())
result = 0

while True:
    if n == 0:
        break
    elif n < 0:
        result = -1
        break

    if not n % 5:
        i = n // 5
        n = n - (i * 5)
        result += i
    else:
        n = n - 3
        result += 1

print(result)
