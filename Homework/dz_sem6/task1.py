"""
Задание 1. Модуль для подсчета количества повторений слов
Создайте модуль с функцией, которая получает список слов и возвращает
словарь, в котором ключи — это слова, а значения — количество их повторений
в списке.
"""
def dict_count(list):
    dict_words = {}
    for word in list:
        dict_words[word] = dict_words.get(word, 0) + 1
    return dict_words

list_str = ['apple', 'banana', 'apple', 'cherry', 'banana', 'cherry', 'apple', 'banana', 'cherry', 'kusok']
dict_words = dict_count(list_str)
print(dict_words)