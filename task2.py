def get_count_char(str_):
    dict_word = {} #завели пустой словарь
    for word in str_:
        if word.isalpha(): #проверяем что символ - буква
            if word in dict_word:
                dict_word[word] += 1
            else:
                dict_word[word] = 1
    return dict_word

    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_str = main_str.lower() #перевели строку в нижний регистр
print(get_count_char(main_str))
