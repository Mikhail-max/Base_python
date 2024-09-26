my_list = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1]
new_list = []
for countt, number in enumerate(my_list, 1):
    if number % 2 != 0:
        new_list.append(countt)
print(my_list)
print(new_list)
