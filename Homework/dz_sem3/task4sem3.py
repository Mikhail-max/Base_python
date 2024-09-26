# Дан список повторяющихся элементов lst.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 2, 3, 4, 5]
lst_new = []
# Введите ваше решение ниже
for num in lst:
    if lst.count(num) > 1:
        if num not in lst_new:
            lst_new.append(num)
print(lst_new)