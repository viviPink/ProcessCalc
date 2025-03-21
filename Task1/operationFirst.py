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

def Summ2(n):
    """
       Вычисление суммы ряда 1/(k^2)! для k от 1 до n
       :param n: Верхняя граница суммирования (целое число)
       :return: Сумма ряда
       """

    def factorial_generator():
        fact = 1
        i = 0
        while True:
            yield fact
            i += 1
            fact *= i

    # Инициализация генератора факториалов
    fact_gen = factorial_generator()
    factorials = []

    sum_value = 0
    for k in range(1, n + 1):
        k_squared = k * k
        # Генерируем факториалы до k^2
        while len(factorials) <= k_squared:
            factorials.append(next(fact_gen))
        sum_value += 1 / factorials[k_squared]

    return sum_value



import numpy as np




def count_elements(sequence):
    """
    Подсчитывает количество элементов в последовательности,
    которые кратны 3 и не кратны 5

    :param sequence: Массив numpy
    :return: Количество подходящих элементов
    """
    count = 0
    for num in sequence:
        if num % 3 == 0 and num % 5 != 0:
            count += 1
    return count






# import numpy as np
#
#
# def count_sum(n, sequence):
#     """
#     Вычисляет сумму ai/0! + a2/1! + ... + an/(n-1)!.
#     :param n: Количество элементов (целое число).
#     :param sequence: Массив numpy
#     :return: Сумма ai/0! + a2/1! + ... + an/(n-1)!.
#     """
#     n = int(n)
#     # Проверяем, что длина последовательности равна n
#     if len(sequence) != n:
#         raise ValueError("Длина последовательности должна быть равна n.")
#     # Создаем массив факториалов от 0 до n-1
#     factorials = np.array([math.factorial(i) for i in range(n)])
#     # Вычисляем сумму ai / i!
#     result = np.sum(sequence / factorials)
#     return result





def count_sum(n, sequence):
    """
    Вычисляет сумму ai/0! + a2/1! + ... + an/(n-1)!.
    :param n: Количество элементов
    :param sequence: Массив numpy
    :return: Сумма ai/0! + a2/1! + ... + an/(n-1)!.
    """
    n = int(n)

    # Генерируем список значений
    terms = [sequence[i] / math.factorial(i) for i in range(n)]
    result = 0
    for term in terms:
        result += term

    return result







"""функция для создание новой матрицы по условию метод сам"""
def calculate_matrix(A):
    A = np.array(A)
    n = A.shape[0]
    B = np.zeros_like(A, dtype=float)
    for i in range(n):
        for j in range(n):
            submatrix = A[i:, :j + 1]
            B[i, j] = np.sum(submatrix)
    return B

