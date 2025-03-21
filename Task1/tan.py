author = "Пинчукова"

"""
Даны действительные числа a, b, c. Удвоить эти числа, если a ≥ b ≥ c, и заменить их абсолютными значениями, если это не так.
"""

# main.py

import sys
from operationSecond import check, double, aBs
from test import TestSecond


def process_numbers(numbers):
    """
    Обрабатывает список чисел согласно условиям задачи.
    :param numbers: Список чисел
    :return: Результат обработки
    """
    if len(numbers) < 2:
        return "Введите больше двух чисел."
    if check(numbers):
        return f"Удвоенные значения: {double(numbers)}"
    else:
        return f"Абсолютные значения: {aBs(numbers)}"


def print_help() :
    """
    Выводит справочную информацию о программе.
    """
    help_text = (
        "Использование: python Count.py [последовательность чисел]\n"
        "Даны действительные числа a, b, c. \n"
        "Удвоить эти числа, если a ≥ b ≥ c, и заменить их абсолютными значениями, если это не так"
    )
    print(help_text)


def main():
    if len(sys.argv) == 1 or sys.argv[1] in ("-h", "--help"):
        print_help()
        return

    if len(sys.argv) > 1:
        try:
            # Преобразуем аргументы командной строки в список чисел
            sequence = list(map(int, sys.argv[1:]))
        except ValueError:
            print("Неверный формат аргумента")
            sys.exit(1)
        """split-список строк 
           list- запросит значения и вернет их в список 
           .sequence_input.split(' '):
          - Он разбивает строку на список строк (подстрок), используя пробел ' ' в качестве разделителя.
           map(int, ...):
          -map(int, ...) преобразует каждую строку из списка в целое число, применяя функцию int к каждому элементу.
           list(...):
          - Внешняя функция list() преобразует итератор, полученный с помощью map(), в список.
           """
    count = process_numbers(sequence)
    print(f"ответ: {count}")


# Объяснение:
# Конструкция 'if __name__ == "__main__": main()' гарантирует, что функция main() будет вызвана только тогда,
# когда скрипт запускается напрямую. Если модуль импортирован, код внутри этого блока не выполнится.

if __name__ == "__main__":
    main()
    TestSecond()