

from operationSecond import check, double, aBs
from operationFirst import Perimeter, Summ, count_elements, calculate_matrix
import math
import numpy as np


# test.py

from operationSecond import check, double, aBs

def TestSecond():
    """
    Тестирование функций check, double и aBs.
    """
    numbers = [6, 4, 2]
    assert check(numbers), "Тест 1 False"

    numbers = [2, 4, 6]
    assert not check(numbers), "Тест 2 False"

    numbers = [1, 2, 3]
    expected_result = [2, 4, 6]
    assert double(numbers) == expected_result, f"Тест 3 False"

    numbers = [-1, -2, 3]
    expected_result = [1, 2, 3]
    assert aBs(numbers) == expected_result, f"Тест 4 False"
    numbers = [5]
    assert check(numbers) == True, "Тест 6 False (check для одного элемента)"
    assert double(numbers) == [10], "Тест 6 False (double для одного элемента)"
    assert aBs(numbers) == [5], "Тест 6 False (aBs для одного элемента)"
    numbers = [-3, -6, -9]
    assert check(numbers), "Тест 7 False"
    assert double(numbers) == [-6, -12, -18], "Тест 7 False (double для отрицательных чисел)"
    assert aBs(numbers) == [3, 6, 9], "Тест 7 False (aBs для отрицательных чисел)"



def TestFirst():
    """
    Проверка работы функции Perimeter.
    """
    expected_perimeter = 2 * 3 * 1 * math.sin(math.pi / 3)
    assert abs(Perimeter(1, 3) - expected_perimeter) < 1e-6, "Тест 1 False"
    expected_perimeter = 2 * 4 * 1 * math.sin(math.pi / 4)
    assert abs(Perimeter(1, 4) - expected_perimeter) < 1e-6, "Тест 2 Falsae"
    expected_perimeter = 2 * 6 * 1 * math.sin(math.pi / 6)
    assert abs(Perimeter(1, 6) - expected_perimeter) < 1e-6, "Тест 3 False"
    expected_perimeter = 2 * 8 * 2 * math.sin(math.pi / 8)
    assert abs(Perimeter(2, 8) - expected_perimeter) < 1e-6, "Тест 4 False"
    expected_perimeter = 2 * 100 * 5 * math.sin(math.pi / 100)
    assert abs(Perimeter(5, 100) - expected_perimeter) < 1e-6, "Тест 5 False"
    expected_perimeter = 2 * math.pi * 1  # При больших n периметр приближается к длине окружности
    assert abs(Perimeter(1, 10000) - expected_perimeter) < 1e-3, "Тест 6 False"


def TestThird():
        """
        Тестирование функции Summ
        """
        assert abs(Summ(1) - 1.0) < 1e-6, "Тест 1 False"
        assert abs(Summ(2) - 1.5) < 1e-6, "Тест 2 False"
        expected_value_3 = 1 + 1 / 2 + 1 / 3
        assert abs(Summ(3) - expected_value_3) < 1e-6, "Тест 3 False"
        expected_value_4 = 1 + 1 / 2 + 1 / 3 + 1 / 4
        assert abs(Summ(4) - expected_value_4) < 1e-6, "Тест 4 False"
        expected_value_10 = sum(1 / k for k in range(1, 11))
        assert abs(Summ(10) - expected_value_10) < 1e-6, "Тест 5 False"
        expected_value_100 = sum(1 / k for k in range(1, 101))
        assert abs(Summ(100) - expected_value_100) < 1e-6, "Тест 6 False"


def TestCount():
    """
    Тестирование функции count_elements
    """
    sequence = []
    result = count_elements(sequence)
    assert result == 0, "Тест 1 False"
    sequence = [1, 2, 4, 5, 7, 10]
    result = count_elements(sequence)
    assert result == 0, "Тест 2 False"
    sequence = [3]
    result = count_elements(sequence)
    assert result == 1, "Тест 3 False"
    sequence = [3, 6, 9, 12, 15, 18, 20]
    result = count_elements(sequence)
    assert result == 5, "Тест 4 False"




def TestFive():
    """
    Тесты для функции count_sum.
    """

    n = 3
    sequence = np.array([1, 2, 3])
    expected = 1 / 1 + 2 / 1 + 3 / 2  # 1 + 2 + 1.5 = 4.5
    assert np.isclose(count_sum(n, sequence), expected), "Тест 1 не пройден"

    n = 4
    sequence = np.array([0, 0, 0, 0])
    expected = 0
    assert np.isclose(count_sum(n, sequence), expected), "Тест 2 не пройден"

    n = 2
    sequence = np.array([-1, -2])
    expected = -1 / 1 + -2 / 1  # -1 + -2 = -3
    assert np.isclose(count_sum(n, sequence), expected), "Тест 3 не пройден"

    n = 1
    sequence = np.array([5])
    expected = 5 / 1  # 5
    assert np.isclose(count_sum(n, sequence), expected), "Тест 4 не пройден"

    n = 5
    sequence = np.array([1, 2, 3, 4, 5])
    factorials = np.array([1, 1, 2, 6, 24])
    expected = np.sum(sequence / factorials)  # 1 + 2 + 1.5 + 0.666... + 0.2083...
    assert np.isclose(count_sum(n, sequence), expected), "Тест 5 не пройден"


def Test8lab():
    A_default = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_B_default = np.array([
[12, 27, 45.]
 [11, 24, 39]
 [ 7, 15, 24]])
    assert np.allclose(calculate_matrix(A_default), expected_B_default), "Тест 1 не пройден"

    # Тест 2: Матрица 2x2
    A_test_2x2 = [
        [1, 2],
        [3, 4]
    ]
    expected_B_test_2x2 = np.array([
        [10., 6.],
        [7., 4.]
    ])
    assert np.allclose(calculate_matrix(A_test_2x2), expected_B_test_2x2), "Тест 2 не пройден"

    # Матрица 1x1
    A_test_1x1 = [[5]]
    expected_B_test_1x1 = np.array([[5.]])
    assert np.allclose(calculate_matrix(A_test_1x1), expected_B_test_1x1), "Тест 3 не пройден"




from operationSecond import same_color
def Test3():
    """Функция проверяет, являются ли два поля шахматной доски полями одного цвета."""

    # Тест 1: Поля одного цвета
    assert same_color(1, 1, 2, 2) == True, "Тест 1 не пройден"

    # Тест 2: Поля разного цвета
    assert same_color(1, 1, 1, 2) == False, "Тест 2 не пройден"

    # Тест 3: Поля одного цвета (угловые клетки)
    assert same_color(1, 1, 8, 8) == True, "Тест 3 не пройден"

    # Тест 4: Поля разного цвета (противоположные углы)
    assert same_color(1, 1, 8, 7) == False, "Тест 4 не пройден"

    # Тест 5: Поля одного цвета (одинаковые координаты)
    assert same_color(4, 4, 4, 4) == True, "Тест 5 не пройден"

    # Тест 6: Поля разного цвета (центральные клетки)
    assert same_color(4, 4, 5, 5) == True, "Тест 6 не пройден"

    # Тест 7: Поля разного цвета (граничные случаи)
    assert same_color(1, 8, 8, 1) == True,"Тест 6 не пройден"

