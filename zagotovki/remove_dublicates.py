def remove_consecutive_duplicates(s):
# Если строка пуста, возвращаем её как есть
    if not s:
        return s
# Инициализируем список для хранения результата
    result = [s[0]]
# Проходим по каждому символу в строке, начиная со второго
    for char in s[1:]:
# Если текущий символ не совпадает с последним добавленным
# символом
#     в
#     result
        if char != result[-1]:
# Добавляем текущий символ в результат
            result.append(char)
# Преобразуем список символов обратно в строку и возвращаем её
    return ''.join(result)