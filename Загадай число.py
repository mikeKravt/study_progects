#Программа "Загадай число" \ MikeKravt 24/02/2016
#Пользователь загадует натуральное число от 1 до 100, а ПК отгадует
#В конце выводится отгаданое число и количество попыток

import random

print ("\n\t\t\tДобро пожаловать в ИГРУ!")
print ("\n\nЗагадайте любое целое число от 1 до 100. Если Вы готовы, напишите ДА")
#Алгоритм для определения готовности пользователя (загадал число или нет)
quest = input ("\nНачинаем? Ваш ответ: ")

while quest != "":
    if quest.lower() == "нет":
        print ("\n\tНу сколько еще ждать?")
        quest = input ("\nНачинаем? Ваш ответ: ")
    else:
        print ("Тогда начнем...")
        break
#Алгоритм присвоения случайного значения. Вывод первого варианта.
number = random.randint (1, 100)
print (number)
answ = str(input("Я угадал? Ваш ответ: "))
min = 1
max = 100
if answ.lower() == "да":
    print ("Ура! Я угадал с первого раза. Я Суперкомп")
#Основной цикл
tries = 1
while answ != "да":
    answ2 = str(input("Больше или меньше? Ваш ответ: "))
    if answ2.lower() == "больше":
        min = number
        number = random.randint (number, max)
        print (number)
        answ = str(input("Я угадал? "))
    elif answ2.lower() == "меньше":
        max = number
        number = random.randint (min, number)
        print (number)
        answ = str(input("Я угадал? "))
    tries +=1
#Вывод заключительного результата
print ("\t\t\tУра! Я угадал. Это число:", number)
print ("\n\t\t\tИ угадал я всего с", tries,"попытки.")
