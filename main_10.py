from lab_menu import read_array, read_number, run_menu


def task_1(array, target):
    """Ищем значение в отсортированном по возрастанию массиве.

    Сравниваем цель с серединой и отбрасываем половину, в которой ее
    быть не может. Возвращаем индекс с нуля или -1, если цель не найдена.
    """
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        if array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def main():
    run_menu([
        ("Бинарный поиск", task_1,
         (("Отсортированный массив через пробел", read_array), ("Искомое число", read_number)),
         ("Индекс с нуля (-1, если не найдено)",)),
    ])


if __name__ == "__main__":
    main()
