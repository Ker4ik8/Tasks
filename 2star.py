def result(i, t, rev, a):
    while t != 0:
        rev = rev * 10
        rev += t % 10
        t = t // 10
    if a % 10 ** (i // 2) == rev:
        print("YES")
    else:
        print("NO")

a = int(input())
b = a
i = 0
while b != 0:
    b = b // 10
    i += 1
print(i)
if i == 1:
    print("YES")
elif i % 2 == 1:
    rev = 0
    t = a // 10**(i // 2 + 1)
    result(i, t, rev, a)
else:
    rev = 0
    t = a // 10 ** (i // 2)
    result(i, t, rev, a)
