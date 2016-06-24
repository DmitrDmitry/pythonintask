#Задача 7. Вариант 5.

#Напишите программу, которая выводит имя "Жан Батист Поклен", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

#Dzhariashvili D. G.
#15.04.2016


from random import choice

print("Угадайте один из трех цветов светофора!")

cities = tuple("Красный Желтый Зеленый" .split())

cities = [x.lower() for x in cities]

right = choice(cities)
trys = []

score_unit = 33
score = score_unit * len(cities)


k = 1
while True:
print('\n', k, 'попытка.. У вас', score, 'очков.')
word = input('> ').lower()

if right == word:
print('Правильно! Это', right + '!')
print('Вы заработали', score, 'очков!')
input('\nНамите Enter...')
break

if word not in cities:
print('Такого цвета нет')
continue

if word in trys:
print('Вы уже пробовали', word)
continue
trys.append(word)
score -= score_unit

k += 1
if k == 4:
print('Подсказка: последниие две буквы -', right[-2:])

elif k == 6:
r = cities.index(right)
print('Подсказка:', cities[r-1], '...',
cities[r+1 if r < len(cities)-1 else 0])