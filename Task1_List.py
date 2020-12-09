print("Введите количество чисел, которое хотите ввести.")
n = int(input())
print("Введите числа в одну строку.")
a = [int(i) for i in input().split()]
a_list = list(a)
b_list = list()
for i in a_list:
    if i % 2 == 0:
        b_list.append(i)
print(b_list)
