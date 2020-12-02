def my_power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return (1 / a) * my_power(a, n + 1)
    else:
        return a * my_power(a, n - 1)


a = int(input())
n = int(input())
num = my_power(a, n)
print(num)
