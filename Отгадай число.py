# Программа "Отгадай число"
import random
print ("\t\t\tWelcome to the Game!")
print ("\n\nI have a number from 1 to 100")
print ("What is this number?")
number = random.randint(1, 100)
variant = int(input("Ваш вариант: "))
tries = 1
while variant != number:
    if variant > number:
        print ("Меньше...")
    else:
        print ("Больше...")
    variant = int(input("Ваш вариант: "))
    tries += 1
print ("Вам удалось отгадать число! Это в самом деле", number)
print ("Вы затратили на отгадывание", tries, "попыток")
input ("\n\nНажмите ENTER, чтобы выйти")
                  
