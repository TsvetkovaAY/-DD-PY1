def delete(list_, index=None):
    if index == None:
        index = -1
        list_ = list_[0:-1]
    else:
        list_left = list_[:index]
        list_right = list_[index + 1:]
        list_ = list_left + list_right
    return list_



print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
