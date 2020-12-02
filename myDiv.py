def my_div(x):
    sup = 0
    for i in range(x // 2, 0, -1):
        if x % i == 0:
            sup = i
            break
    if sup != 1:
        return sup
    else:
        return x


a = int(input())
b = my_div(a)
print(b)
