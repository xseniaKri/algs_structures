from queue import Empty, Queue

from lab_menu import run_menu


def task_1(commands):
    """Выполняем команды над очередью FIFO, начиная с пустой очереди.

    +значение добавляет элемент, - извлекает первый добавленный элемент,
    ? показывает размер. Извлечение из пустой очереди не ждет добавления.
    """
    queue = Queue()
    results = []
    for command in commands:
        if command.startswith("+") and len(command) > 1:
            queue.put(command[1:])
        elif command == "-":
            try:
                results.append(queue.get_nowait())
            except Empty:
                results.append("Очередь пуста")
        elif command == "?":
            results.append(queue.qsize())
        else:
            raise ValueError(f"Неизвестная команда: {command}")
    remaining = [queue.get_nowait() for _ in range(queue.qsize())]
    return results, remaining


def main():
    run_menu([
        ("Работа с очередью", task_1,
         (("Команды через пробел (пример: +А +Б ? -)", str.split),),
         ("Результаты извлечения и проверки размера", "Остаток очереди")),
    ])


if __name__ == "__main__":
    main()
