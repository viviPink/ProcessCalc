author = "Пинчукова"

"""(5)Даны натуральное число n, действительные числа a1,..., an ai/0!+...an/(n-1)!"""


import sys
import numpy as np
from operationFirst import count_sum
# from test import TestFive

def print_help():
    """
    Выводит справочную информацию о программе
    """
    help_text = (
        "Использование: python Tsfive.py -n [число 'ktvtynjd]  -num [последовательность чисел]\n"
        "Находит сумму ai/0!+...an/(n-1)!\n"
    )
    print(help_text)

def main():
    # Если аргументов нет или указан флаг -h/--help
    if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help")):
        print_help()
        return

    # Преобразуем аргументы командной строки в массив numpy
    try:
        n = sys.argv[1]
        sequence = np.array(sys.argv[2:], dtype=int)
    except ValueError:
        print("Неверный формат аргумента")
        sys.exit(1)

    count = count_sum(n,sequence)
    print(f"Сумма элементов {count}")

if __name__ == "__main__":
    # TestFive()  # Запускаем тесты
    main()