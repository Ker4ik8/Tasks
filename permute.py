def permute(a, i, n):
    if i == n:
        print(a)
    else:
        for j in range(i, n):
            b = a[i]
            a[i] = a[j]
            a[j] = b
            permute(a, i + 1, n)
            b = a[i]
            a[i] = a[j]
            a[j] = b


n = int(input())
a = [0] * n
for i in range(0, n):
    a[i] = i + 1
permute(a, 0, n)
