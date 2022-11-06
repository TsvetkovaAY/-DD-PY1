def get_count_char(str_):
    dict_word = {} #завели пустой словарь
    for word in str_:
        if word.isalpha(): #проверяем что символ - буква
            if word in dict_word:
                dict_word[word] += 1
            else:
                dict_word[word] = 1
    return dict_word

def percent_dict(dict_):
    summ = sum(dict_.values())
    for val in dict_:
        dict_[val] = round(dict_[val] / summ * 100, 2)  #округляем, чтобы после запятой было ограниченное количество знаков (2)
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_str = main_str.lower()  #перевели строку в нижний регистр
print(get_count_char(main_str))
dict_new = get_count_char(main_str) #создаем словарь, которому присвоим словарь, полученный в результате работы функции get_count_char
print(percent_dict(dict_new))
