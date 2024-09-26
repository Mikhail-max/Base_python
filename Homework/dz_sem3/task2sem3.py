#
# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
# (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
#
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.



text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"

# Введите ваше решение ниже
# text = text.replace(".", "")
# text = text.replace("'", " ")
# text = text.replace(",", "")
# text = text.replace("!", "")
#
# text = text.lower().split()

text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)
text = text.split()
print(text)
text_dict = {}
for word in text:
    if word.isalpha():
        text_dict[word] = text_dict.get(word, 0) + 1
# text_dict = dict(sorted(text_dict.items(), reverse=True))
text_dict = sorted(text_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]
print(text_dict)

# if len(text_dict) > 10:
#     for i in text_dict[:10]:
#         new_text_dict.setdefault(i[0], i[1])
#     print(f' Новый словарь {new_text_dict}')
# else:
#     print(text_dict)
