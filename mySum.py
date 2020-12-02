def my_sum(a, b):
    if a != 0:
        if a > 0:
            return 1 + my_sum(a - 1, b)
        else:
            return -1 + my_sum(a + 1, b)
    elif b != 0:
        if b > 0:
            return 1 + my_sum(a, b - 1)
        else:
            return -1 + my_sum(a, b + 1)
    else:
        return 0


n1 = int(input())
n2 = int(input())
ssumm = my_sum(n1, n2)
print(ssumm)
