total_sum = 0
total_cards = int(input('Введите кол-во карточек: '))

for num in range(1, total_cards + 1):
    total_sum += num

for num in range(1, total_cards):
    user = int(input('Введите номер карточки: '))
    total_sum -= user

print(f'Потеряшка карточка под номером: {total_sum}')
