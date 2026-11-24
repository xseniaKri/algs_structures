from math import isfinite


def read_real(value):
    number = float(value.replace(",", "."))
    if not isfinite(number):
        raise ValueError("Введите конечное число.")
    return number


def read_number(value):
    try:
        return int(value)
    except ValueError:
        return read_real(value)


def read_array(value):
    return [read_number(item) for item in value.split()]


def read_int_array(value):
    return [int(item) for item in value.split()]


def read_matrix(value, read_row=read_array):
    matrix = [read_row(row) for row in value.split(";")]
    if not matrix[0] or any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Все строки матрицы должны быть непустыми и одинаковой длины.")
    return matrix


def run_menu(tasks):
    while True:
        print("\nВыберите задачу:")
        for number, (title, _, _, _) in enumerate(tasks, start=1):
            print(f"{number}. {title}")
        print("0. Выход")

        try:
            choice = input("Номер задачи: ").strip()
            if choice == "0":
                return
            if choice not in [str(i) for i in range(1, len(tasks) + 1)]:
                print(f"Введите номер от 1 до {len(tasks)} или 0 для выхода.")
                continue

            title, function, parameters, labels = tasks[int(choice) - 1]
            print(f"\n{title}")
            values = [convert(input(f"{name} = ")) for name, convert in parameters]
            result = function(*values)
        except EOFError:
            return
        except (ValueError, IndexError, ArithmeticError, RecursionError) as error:
            print(f"Ошибка: {error}")
            continue

        results = (result,) if len(labels) == 1 else result
        for label, value in zip(labels, results):
            print(f"{label} = {value}")
