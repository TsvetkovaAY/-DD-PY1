list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_index = 0
last_index = len(list_numbers) - 1
for i in range(len(list_numbers)):
    if list_numbers[i] >= list_numbers[max_index]:
        max_index = i;
list_numbers[max_index], list_numbers[last_index] = list_numbers[last_index], list_numbers[max_index]
print(list_numbers)
