print("Введите количество чисел, которое хотите ввести.")
n = int(input())
print("Введите числа в строку.")
a = [int(i) for i in input().split()]
a_list = list(a)
res = [int(item) for item in a_list]
newSet = set(res)
print(len(newSet))
