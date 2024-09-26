# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

file_path = "C:/Users/User/Documents/example.txt"
#
# def get_file_info(file_path):
#
#     find1 = file_path.rfind('/')
#     find2 = file_path.rfind('.')
#     list_text = []
#
#     for txt in file_path:
#         list_text.append(txt)
#
#
#     list_text.insert(find1+1, '***')
#     list_text.insert(find2+1, '***')
#
#     file_path = tuple(','.join(list_text).replace(',', '').split('***'))
#     return file_path
#
#
#
# print(get_file_info(file_path))

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    print(file_name)
    file_extension = file_name.split(".")[-1]
    print(file_extension)
    path = file_path[:-len(file_name)]
    print(path)
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)

print(get_file_info(file_path))