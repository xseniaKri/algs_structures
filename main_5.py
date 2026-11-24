from lab_menu import read_array, read_int_array, read_real, run_menu


def task_1(n):
    return [2 * i + 1 for i in range(n)]


def task_2(n, a, d):
    array = [a]
    for _ in range(1, n):
        array.append(array[-1] * d)
    return array


def task_3(n, a, b):
    array = [a, b]
    total = a + b
    for _ in range(2, n):
        array.append(total)
        total += array[-1]
    return array


def task_4(array):
    result = []
    left, right = 0, len(array) - 1
    while left < right:
        result.extend((array[left], array[right]))
        left += 1
        right -= 1
    if left == right:
        result.append(array[left])
    return result


def task_5(array):
    return array[::2] + array[1::2][::-1]


def task_6(array, k, l):
    if not 1 <= k <= l <= len(array):
        raise ValueError("Должно выполняться условие 1 ≤ K ≤ L ≤ длина массива.")
    return sum(array[k - 1:l]) / (l - k + 1)


def task_7(array):
    if len(array) < 2:
        return 0
    difference = array[1] - array[0]
    for i in range(2, len(array)):
        if array[i] - array[i - 1] != difference:
            return 0
    return difference


def task_8(array):
    return min(array[1::2])


def task_9(array):
    last = len(array) - 1
    for i in range(last, -1, -1):
        larger_than_left = i == 0 or array[i] > array[i - 1]
        larger_than_right = i == last or array[i] > array[i + 1]
        if larger_than_left and larger_than_right:
            return i + 1
    return 0


def task_10(array):
    positions = {}
    for position, value in enumerate(array, start=1):
        if value in positions:
            return positions[value], position
        positions[value] = position


def main():
    n = ("N", int)
    array = ("Массив через пробел", read_array)
    integers = ("Целые числа через пробел", read_int_array)
    run_menu([
        ("Первые N нечетных чисел", task_1, (n,), ("Массив",)),
        ("Геометрическая прогрессия", task_2,
         (n, ("A", read_real), ("D", read_real)), ("Массив",)),
        ("Массив с накоплением суммы", task_3, (n, ("A", int), ("B", int)), ("Массив",)),
        ("Обход массива с двух концов", task_4, (array,), ("Элементы",)),
        ("Элементы на нечетных и четных местах", task_5, (array,), ("Элементы",)),
        ("Среднее на участке от K до L", task_6, (array, ("K", int), ("L", int)), ("Среднее",)),
        ("Проверка арифметической прогрессии", task_7, (integers,), ("Разность",)),
        ("Минимум на четных местах", task_8, (array,), ("Минимум",)),
        ("Последний локальный максимум", task_9, (array,), ("Номер",)),
        ("Номера одинаковых элементов", task_10, (integers,), ("Номера",)),
    ])


if __name__ == "__main__":
    main()
