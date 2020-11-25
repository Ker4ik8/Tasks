a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 100 == ((i // 100) % 10 * 10 + i // 1000):
        print(i)
