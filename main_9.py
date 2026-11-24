from lab_menu import read_array, run_menu


def task_1(array):
    """Ищем наименьший элемент в неупорядоченной части массива.

    Меняем его местами с первым элементом этой части и переходим
    к следующей позиции.
    """
    result = list(array)
    for start in range(len(result) - 1):
        smallest = start
        for i in range(start + 1, len(result)):
            if result[i] < result[smallest]:
                smallest = i
        result[start], result[smallest] = result[smallest], result[start]
    return result


def main():
    run_menu([
        ("Сортировка выбором", task_1, (("Массив через пробел", read_array),), ("Массив",)),
    ])


if __name__ == "__main__":
    main()
