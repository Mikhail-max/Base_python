"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.

"""
from functools import reduce


def read_files(filename1: str, filename2: str):
    with open(filename1, 'r', encoding='utf-8') as number_f,\
        open(filename2, 'r', encoding='utf-8') as name_f:
        num_products = [reduce(lambda x, y: x * y, map(float, line.split('|')))
                        for line in number_f.readlines()]
        names = [name.strip('\n') for name in name_f.readlines()]
        delta = abs(len(names) - len(num_products))
        if delta:
            for i in range(delta):
                if len(names) > len(num_products):
                    num_products.append(num_products[i])
                else:
                    names.append(names[i])


        return zip(names, num_products)

def write_file(file: str, func):
    with open(file, 'w', encoding='utf-8') as result_f:
        for name, number in func:
            name: str = name.lower() if number < 0 else name.upper()
            number = int(-number) if number < 0 else int(number)
            print(f'{name} {number}', file = result_f)


if __name__ == '__main__':
    write_file('results.txt', read_files('number.txt', 'Names.txt'))




