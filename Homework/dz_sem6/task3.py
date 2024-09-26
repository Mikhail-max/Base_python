"""
Создайте модуль с функцией, которая принимает два списка и возвращает
список, содержащий только элементы, которые уникальны для обоих списков.
"""
def unic_element_list(lst1, lst2):
    return list(set(lst1) ^ set(lst2)) #list(set(lst1) - set(lst2) | set(lst2) - set(lst1))


print(unic_element_list([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))  # [1, 2, 6, 7]
