

def check(lst):
    """
    Проверяет, упорядочены ли элементы списка по убыванию.
    :param lst: Список чисел
    :return: True, если элементы упорядочены по убыванию, иначе False
    """
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True


def double(lst):
    """
    Удваивает все элементы списка.
    :param lst: Список чисел
    :return: Список с удвоенными значениями
    """
    return [i * 2 for i in lst]


def aBs(lst):
    """
    Заменяет все элементы списка на их абсолютные значения.
    :param lst: Список чисел
    :return: Список с абсолютными значениями
    """
    return [abs(i) for i in lst]