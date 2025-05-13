salary_year = 0

for month in range(1, 13):
    user = int(input(f'Введите данные за {month} месяц: '))
    salary_year += user

result = salary_year / 12
print(f'{result=}')
