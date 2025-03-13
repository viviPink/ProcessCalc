import math

def Perimeter(r, n):
    """
    Вычисляет периметр правильного n-угольника, описанного около окружности радиуса r.
    :param r: Радиус описанной окружности.
    :param n: Количество сторон многоугольника.
    :return: Периметр многоугольника.
    """
    if r <= 0:
        raise ValueError('Радиус не может быть 0 или меньше')
    if n < 3:
        raise ValueError('Количество сторон не может быть меньше 3')
    P = 2 * r * n * math.tan(math.pi / n)
    return round(P, 2)




def Summ(n):
    """
    Вычисление суммы ряда 1/k для k от 1 до n
    """
    sum_value = 0
    for k in range(1, n + 1):
        sum_value += 1 / k
    return sum_value




import numpy as np

def count_elements(sequence):
    """
    Подсчитывает количество элементов в последовательности,
    которые кратны 3 и не кратны 5

    :param sequence: Массив numpy
    :return: Количество подходящих элементов
    """
    # Используем логические операции numpy
    by_3 = (sequence % 3 == 0)
    not_by_5 = (sequence % 5 != 0)
    return np.sum(by_3 & not_by_5)


import numpy as np


def count_sum(n, sequence):
    """
    Вычисляет сумму ai/0! + a2/1! + ... + an/(n-1)!.
    :param n: Количество элементов (целое число).
    :param sequence: Массив numpy
    :return: Сумма ai/0! + a2/1! + ... + an/(n-1)!.
    """
    n = int(n)
    # Проверяем, что длина последовательности равна n
    if len(sequence) != n:
        raise ValueError("Длина последовательности должна быть равна n.")
    # Создаем массив факториалов от 0 до n-1
    factorials = np.array([math.factorial(i) for i in range(n)])
    # Вычисляем сумму ai / i!
    result = np.sum(sequence / factorials)
    return result