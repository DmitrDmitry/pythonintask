#Задача 3. Вариант 5.

#Напишите программу, которая выводит имя "Жан Батист Поклен", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

#Dzhariashvili D. G.
#15.04.2016

name = "Жан Батист Поклен"
psname = "Мольер"
print(name, " - настоящее имя францезского комедиографа")
answer = input("\nВведите имя под которым прославился комедиограф: ")
while answer.find(psname) == -1 and answer.find("0") == -1:
print(answer, "- неверный ответ.", name, "известен под другим именем.")
answer = input("\nопробуйте еще раз (или введите \"0\" для выхода): ")
if answer.find(psname) != -1:
print(answer, "- правильный ответ!")
input("\n\nНажмите Enter для выхода.")