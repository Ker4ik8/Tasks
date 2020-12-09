MyDictEngRus = {"frog" : "лягушка", "bear" : "медведь", "fish" : "рыба", "meat" : "мясо", "knife" : "нож", "spoon" : "ложка", "horse" : "лошадь"}
MyDictRusEng = {"лягушка" : "frog", "медведь" : "bear", "рыба" : "fish", "мясо" : "meat", "нож" : "knife", "ложка" : "spoon", "лошадь" : "horse"}
print("Введите искомое слово")
i = 0
str = input()
if str in MyDictEngRus.keys():
    i = 1
elif str in MyDictRusEng.keys():
    i = 2
if i == 1:
    print(MyDictEngRus.get(str))
elif i == 2:
    print(MyDictRusEng.get(str))
else:
    print("Данного слова нет в словаре.")
