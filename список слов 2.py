import random
spisok = ["котлета", "суп", "суши", "салат", "кока-кола", "пирог"]

while spisok:
    print (spisok.pop(random.randint(0, len(spisok)-1)))
