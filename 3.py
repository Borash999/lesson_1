# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT) 

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
COUNTER = 10
i = 0
while i < COUNTER:
    i += 1
    user = int(input("Введите число больше 0 и меньше 1000: "))
    if user > num:
        print(f"Число больше\nОсталось попыток {COUNTER - i}")
    elif user < num:
        print(f"Число меньше\nОсталось попыток {COUNTER - i}")
    else:
        print("Вы выиграли")
        break