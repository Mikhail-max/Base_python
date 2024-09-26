"""
У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой,
выполняя следующие операции, для выполнения которых необходимо написать следующие функции:

check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.
withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и
проведенных операциях.

Пополнение счета:

Функция deposit(amount) позволяет клиенту пополнять свой счет на
определенную сумму. Пополнение счета возможно только на сумму,
которая кратна MULTIPLICITY.

Снятие средств:

Функция withdraw(amount) позволяет клиенту снимать средства со счета.
Сумма снятия также должна быть кратной MULTIPLICITY.
При снятии средств начисляется комиссия в процентах от снимаемой суммы,
которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

Завершение работы:

Функция exit() завершает работу с банковским счетом. Перед завершением,
если на счету больше RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Проверка кратности суммы:

Функция check_multiplicity(amount) проверяет, кратна ли
сумма amount заданному множителю MULTIPLICITY.
Реализуйте программу для управления банковским счетом,
используя библиотеку decimal для точных вычислений.

"""
import decimal
from decimal import Decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)
bank_account = decimal.Decimal(0)
count = 0
operations = []




def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    else:
        result = f'Сумма должна быть кратной {MULTIPLICITY} у.е.'
        operations.append(result)
        return False



def deposit(amount):
    global bank_account
    if check_multiplicity(amount):
        bank_account = decimal.Decimal(bank_account) + decimal.Decimal(amount)
        result = f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.'
        operations.append(result)
    # else:
        # operations.remove(operations[0])
        # return bank_account


def withdraw(amount):
    global bank_account
    nalog: int= decimal.Decimal(amount) * decimal.Decimal(PERCENT_REMOVAL)
    if nalog < 30:
        nalog = 30
    elif nalog > 600:
        nalog = 600
    full_amount: Decimal = decimal.Decimal(amount) + decimal.Decimal(nalog)
    if check_multiplicity(amount):
        if full_amount < bank_account:
            bank_account = decimal.Decimal(bank_account) - decimal.Decimal(full_amount)
            result = f'Снятие с карты {amount} у.е. Процент за снятие {int(nalog)} у.е.. Итого {int(bank_account)} у.е.'
            operations.append(result)
        else:
            result = f'Недостаточно средств. Сумма с комиссией {int(full_amount)} у.е. На карте {bank_account} у.е.'
            operations.append(result)
    else:
        if full_amount > bank_account:
            # operations.remove(operations[0])
            result = f'Недостаточно средств. Сумма с комиссией {int(full_amount)} у.е. На карте {bank_account} у.е.'
            operations.append(result)


def exit():
    global bank_account
    if bank_account > RICHNESS_SUM:
        rich_nalog = decimal.Decimal(bank_account) * decimal.Decimal(RICHNESS_PERCENT)
        bank_account = decimal.Decimal(bank_account) - decimal.Decimal(rich_nalog)
        result = f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {rich_nalog} у.е. Итого {bank_account} у.е.'
        operations.append(result)
    result = f'Возьмите карту на которой {bank_account} у.е.'
    operations.append(result)


deposit(173)
withdraw(21)
exit()

print(operations)
