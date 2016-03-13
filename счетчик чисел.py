itog = int("0")
first = int(input("Введите начальное значение: "))
last = int(input("Введите последнее значение: "))
interval = int(input("Введите интервал между целыми  числами: "))
last += 1
for i in range(first, last, interval):
    itog += i
print("Сумма введеных вами чисел: ", itog)
input("\n\nВведите Enter, чтобы выйти...")
