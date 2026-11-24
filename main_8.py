from lab_menu import read_array, run_menu


def task_1(array):
    """Берем очередной элемент после упорядоченной части массива.

    Сдвигаем вправо все элементы, которые больше него, и вставляем
    его на освободившееся место.
    """
    result = list(array)
    for i in range(1, len(result)):
        value = result[i]
        position = i
        while position > 0 and result[position - 1] > value:
            result[position] = result[position - 1]
            position -= 1
        result[position] = value
    return result


def main():
    run_menu([
        ("Сортировка вставками", task_1, (("Массив через пробел", read_array),), ("Массив",)),
    ])


if __name__ == "__main__":
    main()
