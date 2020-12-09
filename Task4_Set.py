print("Введите количество чисел, которое хотите ввести в первом множестве.")
n = int(input())
print("Введите числа в одну строку.")
a = [int(i) for i in input().split()]
a.sort()
a_set = set(a)
print("Введите количество чисел, которое хотите ввести во втором множестве.")
m = int(input())
print("Введите числа в одну строку.")
b = [int(i) for i in input().split()]
b.sort()
b_set = set(b)
print(b_set & a_set)
