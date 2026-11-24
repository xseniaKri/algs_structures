from functools import partial
from math import prod

from lab_menu import read_int_array, read_matrix, run_menu


def task_1(matrix):
    if len(matrix) % 2 == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("Введите квадратную матрицу нечетного размера.")
    result = []
    first, last = 0, len(matrix) - 1
    while first < last:
        for row in range(first, last):
            result.append(matrix[row][first])
        for column in range(first, last):
            result.append(matrix[last][column])
        for row in range(last, first, -1):
            result.append(matrix[row][last])
        for column in range(last, first, -1):
            result.append(matrix[first][column])
        first += 1
        last -= 1
    if first == last:
        result.append(matrix[first][first])
    return result


def task_2(matrix, k):
    if not 1 <= k <= len(matrix):
        raise ValueError("Номер строки выходит за границы матрицы.")
    row = matrix[k - 1]
    return sum(row), prod(row)


def task_3(matrix):
    products = [prod(column) for column in zip(*matrix)]
    minimum = min(products)
    return products.index(minimum) + 1, minimum


def task_4(matrix):
    counts = []
    for column in zip(*matrix):
        average = sum(column) / len(column)
        counts.append(sum(value > average for value in column))
    return counts


def task_5(matrix):
    for number, column in enumerate(zip(*matrix), start=1):
        if all(value % 2 for value in column):
            return number
    return 0


def task_6(matrix):
    result = [list(row) for row in matrix]
    for row in result:
        low = row.index(min(row))
        high = row.index(max(row))
        row[low], row[high] = row[high], row[low]
    return result


def task_7(matrix):
    columns = list(zip(*matrix))
    low = min(range(len(columns)), key=lambda i: min(columns[i]))
    high = max(range(len(columns)), key=lambda i: max(columns[i]))
    columns[low], columns[high] = columns[high], columns[low]
    return [list(row) for row in zip(*columns)]


def task_8(matrix):
    result = [list(row) for row in matrix]
    if not result or len(result) % 2 or len(result[0]) % 2:
        raise ValueError("Размеры матрицы должны быть четными.")
    half_rows = len(result) // 2
    half_columns = len(result[0]) // 2
    for row in range(half_rows):
        opposite = row + half_rows
        result[row][:half_columns], result[opposite][half_columns:] = (
            result[opposite][half_columns:], result[row][:half_columns]
        )
    return result


def task_9(matrix):
    return sorted((list(row) for row in matrix), key=lambda row: row[0])


def task_10(matrix):
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("Введите квадратную матрицу.")
    sums = [0] * max(0, 2 * size - 1)
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            sums[size - 1 + i - j] += value
    return sums


def main():
    matrix = ("Матрица (элементы через пробел, строки через ;)", read_matrix)
    integers = (matrix[0], partial(read_matrix, read_row=read_int_array))
    run_menu([
        ("Обход матрицы по спирали", task_1, (matrix,), ("Элементы",)),
        ("Сумма и произведение K-й строки", task_2, (matrix, ("K", int)), ("Сумма", "Произведение")),
        ("Столбец с наименьшим произведением", task_3, (matrix,), ("Номер", "Произведение")),
        ("Количество элементов выше среднего по столбцам", task_4, (matrix,), ("Количество",)),
        ("Первый столбец из нечетных чисел", task_5, (integers,), ("Номер",)),
        ("Обмен минимума и максимума в каждой строке", task_6, (matrix,), ("Матрица",)),
        ("Обмен столбцов с минимумом и максимумом", task_7, (matrix,), ("Матрица",)),
        ("Обмен левой верхней и правой нижней четвертей", task_8, (matrix,), ("Матрица",)),
        ("Упорядочивание строк по первому элементу", task_9, (matrix,), ("Матрица",)),
        ("Суммы диагоналей, параллельных главной", task_10, (matrix,), ("Суммы",)),
    ])


if __name__ == "__main__":
    main()
