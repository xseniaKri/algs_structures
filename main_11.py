from json import loads

from lab_menu import run_menu


def task_1(tree):
    """Обходим двоичное дерево в прямом порядке: корень, левое, правое.

    Узел задается тройкой [значение, левое поддерево, правое поддерево].
    Правое поддерево кладем в стек первым, чтобы левое обработать раньше.
    Пустое поддерево обозначается None, при вводе в JSON — null.
    """
    result = []
    pending = [tree]
    while pending:
        node = pending.pop()
        if node is None:
            continue
        if not isinstance(node, (list, tuple)) or len(node) != 3:
            raise ValueError("Узел должен иметь вид [значение, левое поддерево, правое поддерево].")
        value, left, right = node
        result.append(value)
        pending.extend((right, left))
    return result


def main():
    run_menu([
        ("Прямой обход двоичного дерева", task_1,
         (("Дерево (пример: [1, [2, null, null], [3, null, null]])", loads),),
         ("Порядок обхода",)),
    ])


if __name__ == "__main__":
    main()
