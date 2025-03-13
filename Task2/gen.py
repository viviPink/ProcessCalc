__author__ = "Пинчукова Гера"

from math import factorial
from test import test_generators

"""Генераторы — это специальные функции,
 которые используют ключевое слово yield вместо return. 
 В отличие от обычных функций, которые выполняются один раз и 
 возвращают результат, генераторы могут приостанавливать своё выполнение
  после каждого вызова yield, сохраняя своё состояние, и продолжать работу с того места,
   где они остановились, при следующем обращении."""


def task_a(n):
    for i in range(1, n + 1):
        yield i


def task_b(n):
    for i in range(1, n + 1):
        yield i ** i


def task_c(n):
    for i in range(1, n + 1):
        yield factorial(i)


def task_d(n):
    for i in range(1, n + 1):
        yield 2 ** (i + 1)


def task_e(n):
    for i in range(1, n + 1):
        yield 2 ** i + 3 ** (i + 1)


def task_f(n):
    for i in range(1, n + 1):
        yield 2 ** i / factorial(i)


def task_g(n):
    for i in range(1, n + 1):
        yield sum(1 / j for j in range(1, i + 1))


def task_h(n):
    for i in range(1, n + 1):
        yield sum((-1) ** (j + 1) / j for j in range(1, i + 1))


def task_i(n):
    for i in range(1, n + 1):
        yield i * sum(1 / factorial(j) for j in range(1, i + 1))



# Основная функция
def main():
    # Ввод данных
    n = int(input("Введите количество элементов n: "))

    # Описание последовательностей
    descriptions = {
        "139 а": "a(i) = i",
        "139 б": "b(i) = i^i",
        "139 в": "c(i) = i!",
        "139 г": "d(i) = 2^(i+1)",
        "139 д": "e(i) = 2^i + 3^(i+1)",
        "139 е": "f(i) = 2^i / i!",
        "139 ж": "g(i) = сумма(1/j) для j от 1 до i",
        "139 з": "h(i) = сумма((-1)^(j+1)/j) для j от 1 до i",
        "139 и": "i(i) = i * сумма(1/j!) для j от 1 до i"
    }

    # Форматированный вывод с описанием
    print(f"{'Последовательность':<20} {'Формула':<50} {'Элементы':<40}")
    print()
    sequences = {
        "139 а": task_a(n),
        "139 б": task_b(n),
        "139 в": task_c(n),
        "139 г": task_d(n),
        "139 д": task_e(n),
        "139 е": task_f(n),
        "139 ж": task_g(n),
        "139 з": task_h(n),
        "139 и": task_i(n)
    }

    for name, sequence in sequences.items():
        formula = descriptions[name]
        if name in ["139 е", "139 ж", "139 з", "139 и"]:
            elements = [f"{x:.2f}" for x in sequence]
        else:
            # преобразование переменной sequence в список
            elements = list(sequence)
            #  name будет выведено с выравниванием по левому краю, занимая 20 символов
            #  formula будет отображено также с выравниванием по левому краю, занимая 40 символов
            #', '.join(...): затем все преобразованные строки объединяются в одну строку, разделенную запятыми и пробелами
        print(f"{name:<20} {formula:<40} {', '.join(map(str, elements)):<40}")


# Запуск программы
# С помощью этой конструкции можно определить, запущен ли файл напрямую
# или он импортирован. Если файл запущен напрямую, то выполняется код внутри этого условия
if __name__ == "__main__":
    test_generators()
    main()
