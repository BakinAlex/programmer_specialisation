array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
array = array_1 + array_2 + array_3
result_1 = []
result_1_set = set(array_1) & set(array_2) & set(array_3)
result_2 = []
result_2_set = set(array_1) - (set(array_2) | set(array_3))

for i in range(len(array)):
    if array[i] in array_1 and array[i] in array_2 and array[i] in array_3:
        if array[i] not in result_1:
            result_1.append(array[i])

for i in range(len(array_1)):
    if array_1[i] not in array_2 and array_1[i] not in array_3:
        result_2.append(array_1[i])

print(f'Задача 1.\nРешение без множеств: {', '.join(str(x) for x in result_1)}.\nРешение с множествами: {', '.join(str(x) for x in result_1_set)}.\nЗадача 2:\nРешение без множеств: {', '.join(str(x) for x in result_2)}.\nРешение с множествами: {', '.join(str(x) for x in result_2_set)}.')
