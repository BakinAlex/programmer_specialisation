rating = int(input('Введите рейтинг от -100 до 100: '))
positive = 0
negative = 0

while rating != 0:
    if rating > 0:
        positive += 1
    else:
        negative += 1
    rating = int(input('Введиите значение рейтинга от -100 до 100: '))

print(f'{positive=}, {negative=}')
