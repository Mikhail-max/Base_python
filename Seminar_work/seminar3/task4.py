my_list = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 2, 4, 5, 1]
print(my_list)  # 2,4,5 должно остаться
for number in my_list:
    if my_list.count(number) == 2:
        while number in my_list:
            my_list.pop(my_list.index(number))
print(my_list)
