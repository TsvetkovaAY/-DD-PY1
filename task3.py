
import random

def get_unique_list_numbers() -> list[int]:
    list_num = []
    setnum = set()
    for i in range(15):
        setnum.add(random.randint(-10, 10))
    if len(list_num) < 15:
        setnum.add(random.randint(-10, 10))
    list_num = list(setnum)
    return list_num



list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))



