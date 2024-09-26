from datetime import datetime
def display_current_datetime():
    # Получение текущего времени и даты
    now = datetime.now()
    # Форматирование даты и времени
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    # Получение дня недели и номера недели
    day_of_week = now.strftime('%A')
    week_number = now.isocalendar()[1]
    print(f'Current date and time: {formatted_date}')
    print(f'Day of the week: {day_of_week}')
    print(f'Week number: {week_number}')
if __name__ == '__main__':
    display_current_datetime()
from datetime import datetime, timedelta
def future_date(days_from_now):
    """
    Возвращает дату, которая наступит через указанное количество
    дней от текущей даты.
    :param days_from_now: Количество дней от текущей даты.
    :return: Отформатированная дата в формате YYYY-MM-DD.
    Примеры:
    #>>> future_date(30)
    '2024-09-08'
   # >>> future_date(-10)
    '2024-07-30'

    :param days_from_now:
    :return:
    """
    # Получение текущей даты и времени
    today = datetime.now()
    # Вычисление даты через указанное количество дней
    future_date = today + timedelta(days=days_from_now)
    # Форматирование будущей даты в строку в формате YYYY-MM-DD
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date
if __name__ == '__main__':
        days = 30  # Количество дней для вычисления
        print(f'Date {days} days from now: {future_date(days)}')
