# Задание 1. Модуль для подсчета количества повторений слов
# Создайте модуль с функцией, которая получает список слов и возвращает
# словарь, в котором ключи — это слова, а значения — количество их повторений
# в списке.

def word_count_in_dict(list):
    dict_words = {}
    for word in list:
        dict_words[word] = dict_words.get(word, 0) + 1
    return dict_words

if __name__ == '__main__':
    slova = ['slova', 'slova', 'slova', 'slova', 'slova', 'qqweqweqwe', 'qqweqwe', 'qqwe']
    words = word_count_in_dict(slova)
    print(words)