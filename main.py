from math import sqrt


def task_1(a, b):
    return a * b, 2 * (a + b)


def task_2(d):
    return 3.14 * d


def task_3(a, b):
    return (a + b) / 2


def task_4(a, b):
    a2 = a ** 2
    b2 = b ** 2
    return a2 + b2, a2 - b2, a2 * b2, a2 / b2


def task_5(a, b):
    a = abs(a)
    b = abs(b)
    return a + b, a - b, a * b, a / b


def task_6(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def task_7(a, b, c):
    ac = abs(c - a)
    bc = abs(c - b)
    return ac, bc, ac + bc


def task_8(a, b, c):
    return abs(c - a) * abs(c - b)


def task_9(x1, y1, x2, y2):
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    return 2 * (a + b), a * b


def task_10(x1, y1, x2, y2, x3, y3):
    ab = task_6(x1, y1, x2, y2)
    bc = task_6(x2, y2, x3, y3)
    ca = task_6(x3, y3, x1, y1)
    perimeter = ab + bc + ca

    area = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
    return perimeter, area


def task_11(x):
    return 3 * x ** 6 - 6 * x ** 2 - 7


def task_12(x):
    return 4 * (x - 3) ** 6 - 7 * (x - 3) ** 3 + 2


def main():
    tasks = [
        ("Площадь и периметр прямоугольника", task_1, ("a", "b"), ("S", "P")),
        ("Длина окружности по диаметру", task_2, ("d",), ("L",)),
        ("Среднее арифметическое", task_3, ("a", "b"), ("Среднее",)),
        ("Действия с квадратами ненулевых чисел", task_4, ("a", "b"),
         ("Сумма квадратов", "Разность квадратов", "Произведение квадратов", "Частное квадратов")),
        ("Действия с модулями ненулевых чисел", task_5, ("a", "b"),
         ("Сумма модулей", "Разность модулей", "Произведение модулей", "Частное модулей")),
        ("Расстояние между двумя точками", task_6, ("x1", "y1", "x2", "y2"), ("Расстояние",)),
        ("Длины AC, BC и их сумма", task_7, ("A", "B", "C"), ("AC", "BC", "Сумма")),
        ("Произведение AC и BC (C между A и B)", task_8, ("A", "B", "C"), ("Произведение",)),
        ("Прямоугольник по противоположным вершинам", task_9, ("x1", "y1", "x2", "y2"), ("P", "S")),
        ("Периметр и площадь треугольника", task_10, ("x1", "y1", "x2", "y2", "x3", "y3"), ("P", "S")),
        ("y = 3*x^6 - 6*x^2 - 7", task_11, ("x",), ("y",)),
        ("y = 4*(x-3)^6 - 7*(x-3)^3 + 2", task_12, ("x",), ("y",)),
    ]

    while True:
        print("\nВыберите задачу:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task[0]}")
        print("0. Выход")

        choice = input("Номер задачи: ").strip()
        if choice == "0":
            break
        if choice not in [str(i) for i in range(1, 13)]:
            print("Введите номер от 1 до 12 или 0 для выхода.")
            continue

        title, function, parameters, labels = tasks[int(choice) - 1]
        print(f"\n{title}")
        print("Введите числа по одному (дробную часть можно отделять точкой или запятой).")

        values = [float(input(f"{name} = ").replace(",", ".")) for name in parameters]
        result = function(*values)
        if not isinstance(result, tuple):
            result = (result,)
        for label, value in zip(labels, result):
            print(f"{label} = {value:g}")


if __name__ == "__main__":
    main()
