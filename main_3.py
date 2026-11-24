from fractions import Fraction

from lab_menu import read_real, run_menu


def task_1(price):
    costs = []
    for tenths in range(1, 11):
        costs.append(price * (tenths / 10))
    return costs


def task_2(n):
    product = 1.0
    for i in range(1, n + 1):
        product *= 1 + i / 10
    return product


def task_3(n):
    partial_sums = []
    total = 0
    for odd in range(1, 2 * n, 2):
        total += odd
        partial_sums.append(total)
    return partial_sums


def task_4(a, n):
    total = power = 1
    for _ in range(n):
        power *= a
        total += power
    return total


def task_5(a, n):
    total = power = 1
    for _ in range(n):
        power *= -a
        total += power
    return total


def task_6(a, b):
    numbers = []
    for number in range(a, b + 1):
        for _ in range(number):
            numbers.append(number)
    return numbers


def task_7(a, b):
    remainder = Fraction(str(a))
    length = Fraction(str(b))
    if not 0 < length < remainder:
        raise ValueError("Длины должны удовлетворять условию A > B > 0.")
    while remainder >= length:
        remainder -= length
    if isinstance(a, int) and isinstance(b, int):
        return int(remainder)
    return float(remainder)


def task_8(n):
    k = total = 0
    while total < n:
        k += 1
        total += k
    return k, total


def task_9(p):
    if not 0 < p < 25:
        raise ValueError("Процент должен быть больше 0 и меньше 25.")
    months = 0
    balance = 1000.0
    rate = p / 100
    if balance + balance * rate == balance:
        raise ValueError("Процент слишком мал для расчета с вещественными числами.")
    while balance <= 1100:
        months += 1
        balance += balance * rate
    return months, balance


def task_10(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    a = ("A", read_real)
    b = ("B", read_real)
    n = ("N", int)
    run_menu([
        ("Стоимость конфет от 0,1 до 1 кг", task_1, (("Цена за кг", read_real),), ("Стоимость",)),
        ("Произведение N множителей", task_2, (n,), ("Произведение",)),
        ("Квадрат через сумму нечетных чисел", task_3, (n,), ("Промежуточные суммы",)),
        ("Сумма степеней A", task_4, (a, n), ("Сумма",)),
        ("Знакочередующаяся сумма степеней A", task_5, (a, n), ("Сумма",)),
        ("Повторение чисел от A до B", task_6, (("A", int), ("B", int)), ("Числа",)),
        ("Незанятая часть отрезка", task_7, (a, b), ("Остаток",)),
        ("Первая сумма, не меньшая N", task_8, (n,), ("K", "Сумма")),
        ("Рост банковского вклада", task_9, (("Процент в месяц", read_real),), ("Месяцы", "Вклад")),
        ("Наибольший общий делитель", task_10, (("A", int), ("B", int)), ("НОД",)),
    ])


if __name__ == "__main__":
    main()
