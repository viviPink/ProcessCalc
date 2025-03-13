

from operationSecond import check, double, aBs
from operationFirst import Perimeter, Summ, count_elements
import math



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
 # Тест 1: Простой случай
n = 3
sequence = np.array([1, 2, 3])
expected = 1 / 1 + 2 / 1 + 3 / 2  # 1 + 2 + 1.5 = 4.5
assert np.isclose(count_sum(n, sequence), expected), "Тест 1 не пройден"

# Тест 2: Случай с нулевыми элементами
n = 4
sequence = np.array([0, 0, 0, 0])
expected = 0
assert np.isclose(count_sum(n, sequence), expected), "Тест 2 не пройден"

# Тест 3: Случай с отрицательными числами
n = 2
sequence = np.array([-1, -2])
expected = -1 / 1 + -2 / 1  # -1 + -2 = -3
assert np.isclose(count_sum(n, sequence), expected), "Тест 3 не пройден"

# Тест 4: Одноэлементная последовательность
n = 1
sequence = np.array([5])
expected = 5 / 1  # 5
assert np.isclose(count_sum(n, sequence), expected), "Тест 4 не пройден"

# Тест 5: Большая последовательность
n = 5
sequence = np.array([1, 2, 3, 4, 5])
factorials = np.array([1, 1, 2, 6, 24])
expected = np.sum(sequence / factorials)  # 1 + 2 + 1.5 + 0.666... + 0.2083...
assert np.isclose(count_sum(n, sequence), expected), "Тест 5 не пройден"

