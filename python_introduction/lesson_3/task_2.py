films = ['Безумный Макс', 'Леон', 'Зеленая миля']
my_list = []
count_films = int(input('Какое кол-во фильмов хотите добавить? '))

for num in range(count_films):
    movie = input('Введите название фильма: ')
    if movie in films:
        my_list.append(movie)
    else:
        print(f'Ошибка: фильма {movie} у нас нет :(')
print(f'Ваш список любимых фильмов: {my_list}')
