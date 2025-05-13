import random

guess_count = 1
num = random.randint(0, 11)

while True:
    answer = int(input('Введите число: '))
    if answer == num:
        print(f'Вы угадали! Число попыток: {guess_count}')
        break
    elif answer > num:
        print(f'Число больше, чем нужно. Попробуйте еще раз!')
        guess_count += 1
    else:
        print(f'Число меньше, чем нужно. Попробуйте еще раз!')
        guess_count += 1
