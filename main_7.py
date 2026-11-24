from lab_menu import read_array, run_menu


def task_1(array):
    """Сравниваем соседние элементы и меняем их местами, если левый больше.

    После прохода наибольший элемент стоит в конце, поэтому сокращаем
    границу обхода. Если обменов за проход не было, массив уже упорядочен.
    """
    result = list(array)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
    return result


def main():
    run_menu([
        ("Сортировка пузырьком", task_1, (("Массив через пробел", read_array),), ("Массив",)),
    ])


if __name__ == "__main__":
    main()
