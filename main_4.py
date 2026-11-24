from lab_menu import read_array, read_number, read_real, run_menu


def task_1(n):
    if n < 0:
        raise ValueError("Введите неотрицательное целое число.")
    if n <= 1:
        return 1
    return n * task_1(n - 1)


def task_2(n, current=0, following=1):
    if n < 0:
        raise ValueError("Введите неотрицательный номер числа Фибоначчи.")
    if n == 0:
        return current
    return task_2(n - 1, following, current + following)


def task_3(x, n):
    if n < 0:
        return 1 / task_3(x, -n)
    if n == 0:
        return 1
    half = task_3(x, n // 2)
    square = half * half
    return square * x if n % 2 else square


def task_4(value, left=0, right=None):
    if right is None:
        right = len(value) - 1
    if left >= right:
        return True
    return value[left] == value[right] and task_4(value, left + 1, right - 1)


def task_5(array, target, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left > right:
        return -1
    middle = (left + right) // 2
    if array[middle] == target:
        return middle
    if array[middle] < target:
        return task_5(array, target, middle + 1, right)
    return task_5(array, target, left, middle - 1)


def task_6(value):
    parts = value.rsplit(None, 1)
    if len(parts) < 2:
        return value.strip()
    rest, last_word = parts
    return last_word + " " + task_6(rest)


def task_7(n):
    if n < 2:
        raise ValueError("Разложение существует для целых чисел от 2.")
    if n <= 3:
        return [n]
    return [2] + task_7(n - 2)


def task_8(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + task_8(n // 10)


def task_9(n, source="A", target="C", spare="B"):
    if n < 0:
        raise ValueError("Число дисков должно быть неотрицательным.")
    if n == 0:
        return []
    return (
        task_9(n - 1, source, spare, target)
        + [(source, target)]
        + task_9(n - 1, spare, target, source)
    )


def main():
    n = ("n", int)
    line = ("Строка", str)
    run_menu([
        ("Факториал", task_1, (n,), ("Факториал",)),
        ("Число Фибоначчи", task_2, (n,), ("Число Фибоначчи",)),
        ("Возведение в степень", task_3, (("x", read_real), n), ("Степень",)),
        ("Проверка палиндрома", task_4, (line,), ("Палиндром",)),
        ("Рекурсивный бинарный поиск", task_5,
         (("Отсортированный массив через пробел", read_array), ("Искомое число", read_number)),
         ("Индекс с нуля (-1, если не найдено)",)),
        ("Обратный порядок слов", task_6, (line,), ("Строка",)),
        ("Разложение на простые слагаемые", task_7, (n,), ("Слагаемые",)),
        ("Количество цифр", task_8, (n,), ("Количество",)),
        ("Ханойская башня", task_9, (("Число дисков", int),), ("Переносы",)),
    ])


if __name__ == "__main__":
    main()
