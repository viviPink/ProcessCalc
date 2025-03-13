
__author__ = "Pincukova"

"""
Определить периметр правильного n-угольника, описанного около окружности радиуса r.
"""

import math
import argparse
from test import TestFirst
from operationFirst import Perimeter



def main_cli(args):
    """
    Функция для обработки аргументов командой строки
    """
    r = args.radius
    n = args.sides
    perimeter = Perimeter(r, n)
    print(f"Периметр правильного {n}-угольника с радиусом описанной окружности {r} равен: {perimeter}")


def main_interactive():
    """
    ввод данных через консоль
    """
    r = float(input("Введите радиус описанной окружности: "))
    n = int(input("Введите количество сторон: "))
    perimeter = Perimeter(r, n)
    print(f"Периметр равен {perimeter}")


if __name__ == "__main__":
    TestFirst()
    # Создаем парсер для CLI
    parser = argparse.ArgumentParser(description="Вычисление периметра правильного n-угольника")
    parser.add_argument('-r', '--radius', type=float, help='Радиус описанной окружности.')
    parser.add_argument('-n', '--sides', type=int, help='Количество сторон многоугольника.')

    args = parser.parse_args()

    if args.radius is not None and args.sides is not None:
        # Если переданы аргументы через CLI, используем их
        main_cli(args)
    else:
        # Иначе запускаем интерактивный режим
        print(" укажите параметры -r и -n.")
        main_interactive()

    # Запускаем тесты
