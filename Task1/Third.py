import argparse
from test import TestThird
from operationFirst import Summ

author = "Pinchukova"

def print_help() -> None:
    """
    Выводит справочную информацию о программе.
    """
    help_text = (
        "Использование: python Third.py [-n <n>]\n"
        "Вычисление суммы ряда 1/k для k от 1 до n.\n"
        "  python Third.py -n <n>\n"
    )
    print(help_text)

def main_cli(args):
    """
    Функция для обработки аргументов командной строки
    """
    n = args.n
    if n <= 0:
        raise ValueError("Число n должно быть > 0")
    s = Summ(n)
    print(f"Сумма ряда равна {s:.6f} при n={n}")

# def main_interactive():
#     """
#     Ввод данных через консоль
#     """
#     n = int(input("Введите число n: "))
#     if n <= 0:
#         raise ValueError("Число n должно быть > 0")
#     s = Summ(n)
#     print(f"Сумма ряда равна {s:.6f} при n={n}")

if __name__ == "__main__":
    # Создаем парсер для CLI
    parser = argparse.ArgumentParser(description="115.(4)Вычисление суммы ряда 1/k для k от 1 до n")
    parser.add_argument('-n', type=int, help='Введите n, где n > 0')
    args = parser.parse_args()
    # Проверка наличия аргументов
    if args.n is None:
        print_help()
    else:
        main_cli(args)  # Обработка аргументов командной строки
