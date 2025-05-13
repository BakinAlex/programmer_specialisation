card_count = int(input('Введите кол-во видеокарт: '))
max_item = 0
card_list = []
min_card_list = []

for num in range(1, card_count + 1):
    card = int(input(f'Видеокарта {num}: '))
    if card != max_item:
        max_item = card
        card_list.append(card)
    else:
        card_list.append(card)

for item in card_list:
    if item != max_item:
        min_card_list.append(item)

print(f'Старый список видеокарт: {card_list}')
print(f'Новый список видеокарт: {min_card_list}')
    