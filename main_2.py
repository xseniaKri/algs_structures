from math import sqrt


def task_1(a, b):
    value = max(a, b) if a != b else 0
    return value, value


def task_2(a, b, c):
    return a + b + c - min(a, b, c)


def task_3(xa, ya, xb, yb, xc, yc):
    ab = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
    ac = sqrt((xc - xa) ** 2 + (yc - ya) ** 2)
    if ab <= ac:
        return "B", ab
    return "C", ac


def task_4(x, y):
    if x == 0 or y == 0:
        raise ValueError("Точка не должна лежать на координатных осях.")
    if x > 0:
        return 1 if y > 0 else 4
    return 2 if y > 0 else 3


def task_5(number):
    if number == 0:
        return "нулевое число"
    sign = "положительное" if number > 0 else "отрицательное"
    parity = "четное" if number % 2 == 0 else "нечетное"
    return f"{sign} {parity} число"


def task_6(number):
    if not 1 <= number <= 999:
        raise ValueError("Введите целое число от 1 до 999.")
    parity = "четное" if number % 2 == 0 else "нечетное"
    if number < 10:
        digits = "однозначное"
    elif number < 100:
        digits = "двузначное"
    else:
        digits = "трехзначное"
    return f"{parity} {digits} число"


def task_7(day, month):
    days = (
        "первое", "второе", "третье", "четвертое", "пятое", "шестое",
        "седьмое", "восьмое", "девятое", "десятое", "одиннадцатое",
        "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое",
        "шестнадцатое", "семнадцатое", "восемнадцатое", "девятнадцатое",
        "двадцатое",
    )
    months = (
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря",
    )
    if not 1 <= day <= 31 or not 1 <= month <= 12:
        raise ValueError("День должен быть от 1 до 31, месяц — от 1 до 12.")
    if day <= 20:
        name = days[day - 1]
    elif day < 30:
        name = "двадцать " + days[day - 21]
    elif day == 30:
        name = "тридцатое"
    else:
        name = "тридцать первое"
    return f"{name} {months[month - 1]}"


def task_8(number):
    if not 10 <= number <= 40:
        raise ValueError("Введите целое число от 10 до 40.")
    teens = (
        "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
        "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать",
    )
    units = ("", "одно", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять")
    tens = ("", "", "двадцать", "тридцать", "сорок")
    if number < 20:
        name = teens[number - 10]
        ending = "учебных заданий"
    else:
        unit = number % 10
        name = (tens[number // 10] + " " + units[unit]).strip()
        if unit == 1:
            ending = "учебное задание"
        elif 2 <= unit <= 4:
            ending = "учебных задания"
        else:
            ending = "учебных заданий"
    return f"{name} {ending}"


def task_9(number):
    if not 100 <= number <= 999:
        raise ValueError("Введите целое число от 100 до 999.")
    hundreds = ("", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот")
    tens = ("", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто")
    teens = ("десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать")
    units = ("", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять")
    parts = [hundreds[number // 100]]
    remainder = number % 100
    if 10 <= remainder <= 19:
        parts.append(teens[remainder - 10])
    else:
        parts.extend((tens[remainder // 10], units[remainder % 10]))
    return " ".join(part for part in parts if part)


def task_10(year):
    animals = ("крысы", "коровы", "тигра", "зайца", "дракона", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи")
    colors = ("зелен", "красн", "желт", "бел", "черн")
    offset = (year - 1984) % 60
    animal = offset % 12
    ending = "ого" if animal in (2, 3, 4) else "ой"
    return f"год {colors[offset % 10 // 2]}{ending} {animals[animal]}"


def main():
    tasks = [
        ("Замена значений A и B", task_1, ("A", "B"), int, ("A", "B")),
        ("Сумма двух наибольших чисел", task_2, ("a", "b", "c"), float, ("Сумма",)),
        ("Ближайшая к A точка", task_3, ("xA", "yA", "xB", "yB", "xC", "yC"), float, ("Точка", "Расстояние")),
        ("Координатная четверть", task_4, ("x", "y"), float, ("Четверть",)),
        ("Описание целого числа", task_5, ("Число",), int, ("Описание",)),
        ("Описание числа от 1 до 999", task_6, ("Число",), int, ("Описание",)),
        ("Дата словами", task_7, ("День", "Месяц"), int, ("Дата",)),
        ("Количество учебных заданий словами", task_8, ("Количество",), int, ("Описание",)),
        ("Трехзначное число словами", task_9, ("Число",), int, ("Описание",)),
        ("Название года по восточному календарю", task_10, ("Год",), int, ("Название",)),
    ]

    while True:
        print("\nВыберите задачу:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task[0]}")
        print("0. Выход")

        choice = input("Номер задачи: ").strip()
        if choice == "0":
            break
        if choice not in [str(i) for i in range(1, 11)]:
            print("Введите номер от 1 до 10 или 0 для выхода.")
            continue

        title, function, parameters, value_type, labels = tasks[int(choice) - 1]
        print(f"\n{title}")
        try:
            values = [value_type(input(f"{name} = ").replace(",", ".")) for name in parameters]
            result = function(*values)
        except ValueError as error:
            print(f"Ошибка: {error}")
            continue
        if not isinstance(result, tuple):
            result = (result,)
        for label, value in zip(labels, result):
            if isinstance(value, (int, float)):
                print(f"{label} = {value:g}")
            else:
                print(f"{label} = {value}")


if __name__ == "__main__":
    main()
