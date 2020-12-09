print("Введите количество чисел, которое хотите ввести.")
n = int(input())
print("Введите числа в одной строке.")
a = [int(i) for i in input().split()]
a_list = list(a)
b = 0
for i in range(0, (n // 2) * 2, 2):
    b = a_list[i]
    a_list[i] = a_list[i + 1]
    a_list[i + 1] = b
print(a_list)
