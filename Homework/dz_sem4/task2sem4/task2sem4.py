"""
Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
Вход:
params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)

Выход:
{1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
"""
from Homework.dz_sem4.task2sem4.key_params import key_params

params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)

