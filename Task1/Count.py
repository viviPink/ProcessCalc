
import sys
import numpy as np
from operationFirst import count_elements
from test import TestCount

def print_help():
    """
    Выводит справочную информацию о программе
    """
    help_text = (
        "Использование: python Count.py [последовательность чисел]\n"
        "Находит количество элементов в последовательности,\n"
        "которые кратны 3 и не кратны 5.\n\n"
        "Пример использования:\n"
        "  python Count.py 3 6 9 10 15\n"
        "  Количество элементов, кратных 3 и не кратных 5: 2"
    )
    print(help_text)

def main():
    # Если аргументов нет или указан флаг -h/--help
    if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help")):
        print_help()
        return

    # Преобразуем аргументы командной строки в массив numpy
    try:
        sequence = np.array(sys.argv[1:], dtype=int)
    except ValueError:
        print("Неверный формат аргумента")
        sys.exit(1)

    # Подсчитываем количество элементов, кратных 3 и не кратных 5
    count = count_elements(sequence)
    print(f"Количество элементов, кратных 3 и не кратных 5: {count}")

if __name__ == "__main__":
    TestCount()  # Запускаем тесты
    main()