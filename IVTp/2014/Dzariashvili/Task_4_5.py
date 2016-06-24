#Задача 4. Вариант 5.

#Напишите программу, которая выводит имя "Жан Батист Поклен", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

#Dzhariashvili D. G.
#15.04.2016


real_name = "Фредерик Аустерлиц"
imaginary_name = "Фред Астер"
interests = ("Актер", "Танцор")
born_place = "США"
born_year = 1899
death_year = 1987
death_oldness = death_year - born_year

print(real_name + " \nболее известный под псевдонимом "
+ imaginary_name + ".")

print("""
Нажмите чтобы вывести на экран:
1 - Место рождения,
2 - Год рождения,
3 - Возраст при смерти,
4 - Область интересов,
5 - Выход из программы\n\n""")

while True:
try:
choose = int(input("Ввод: "))
except:
print("Неправильный ввод")
choose = 0

if choose == 1:
print("Место рождения: " + str(born_place))
elif choose == 2:
print("Год рождения: " + str(born_year))
elif choose == 3:
print("Возраст при смерти: " + str(death_oldness))
elif choose == 4:
print("Область интересов: " + " ".join(interests))
elif choose == 5:
break

input("\nНажмите Enter для выхода")