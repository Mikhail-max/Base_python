def guess_num(num, attempts):
    def inner():
        nonlocal attempts
        while attempts > 0:
            number = int(input("Число: "))
            if number == num:
                return 'Угадали!'
            attempts -= 1
        return 'Не угадали!'

    return inner


print(guess_num(15, 1)())