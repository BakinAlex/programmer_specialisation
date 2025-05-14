count = int(input('Введите кол-во заказов: '))
orders = {}

for count in range(count):
    data = input(f'{count + 1} заказ: ')
    data_list = data.split()
    if orders.get(data_list[0]):
        if orders[data_list[0]].get(data_list[1]):
            orders[data_list[0]][data_list[1]] += int(data_list[2])
        orders[data_list[0]][data_list[1]] = int(data_list[2])
    else:
        orders[data_list[0]] = {data_list[1]: int(data_list[2])}

for key in orders.keys():
    print(f'{key}:')
    for key, value in orders[key].items():
        print(f'{key}: {value}')
