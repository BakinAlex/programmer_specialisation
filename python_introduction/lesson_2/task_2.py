hour = 1
task_sum = 0
go_to_store = False

while hour != 9:
    print(f'{hour}-й час')
    task = int(input('Сколько задач подкинули? Число: '))
    task_sum += task
    call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    if call == 1:
        go_to_store = True
    hour += 1

print(f'Рабочий день закончился! Выполнено задач: {task_sum}')
if go_to_store == True:
    print('Нужно зайти в магазин!')
