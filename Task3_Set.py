print("Введите количество чисел, которое хотите ввести.")
n = int(input())
print("Введите числа в одну строку.")
a = [int(i) for i in input().split()]
a_set = set(a)
res = [int(item) for item in a_set]
newSet = set(res)
print(len(newSet))
