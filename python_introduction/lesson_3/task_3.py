start_list = [1, 4, -3, 0, 10]

for i in range(len(start_list) - 1):
    for j in range(len(start_list) - 1 - i):
        if start_list[j] > start_list[j + 1]:
            start_list[j], start_list[j + 1] = start_list[j + 1], start_list[j]

print(start_list)
