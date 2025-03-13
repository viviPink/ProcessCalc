from gen import task_a,task_b,task_e,task_d,task_f,task_g,task_h,task_i


# Тестовая функция
def test_generators():
    # Тестирование функции task_a
    assert list(task_a(1)) == [1], "Ошибка в task_a для n=1"
    assert list(task_a(3)) == [1, 2, 3], "Ошибка в task_a для n=3"
    assert list(task_a(5)) == [1, 2, 3, 4, 5], "Ошибка в task_a для n=5"

    # Тестирование функции task_b
    assert list(task_b(1)) == [1], "Ошибка в task_b для n=1"
    assert list(task_b(2)) == [1, 4], "Ошибка в task_b для n=2"
    assert list(task_b(3)) == [1, 4, 27], "Ошибка в task_b для n=3"

    # Тестирование функции task_d
    assert list(task_d(1)) == [4], "Ошибка в task_d для n=1"
    assert list(task_d(2)) == [4, 8], "Ошибка в task_d для n=2"
    assert list(task_d(3)) == [4, 8, 16], "Ошибка в task_d для n=3"

    # Тестирование функции task_e
    assert list(task_e(1)) == [5], "Ошибка в task_e для n=1"
    assert list(task_e(2)) == [5, 11], "Ошибка в task_e для n=2"
    assert list(task_e(3)) == [5, 11, 35], "Ошибка в task_e для n=3"

    # Тестирование функции task_f
    assert [round(x, 5) for x in task_f(1)] == [2.0], "Ошибка в task_f для n=1"
    assert [round(x, 5) for x in task_f(3)] == [2.0, 1.0, 0.66667], "Ошибка в task_f для n=3"
    assert [round(x, 5) for x in task_f(5)] == [2.0, 1.0, 0.66667, 0.26667, 0.1], "Ошибка в task_f для n=5"

    # Тестирование функции task_g
    assert [round(x, 5) for x in task_g(1)] == [1.0], "Ошибка в task_g для n=1"
    assert [round(x, 5) for x in task_g(2)] == [1.0, 1.5], "Ошибка в task_g для n=2"
    assert [round(x, 5) for x in task_g(5)] == [1.0, 1.5, 1.83333, 2.08333, 2.28333], "Ошибка в task_g для n=5"

    # Тестирование функции task_h
    assert [round(x, 5) for x in task_h(1)] == [1.0], "Ошибка в task_h для n=1"
    assert [round(x, 5) for x in task_h(2)] == [1.0, 0.5], "Ошибка в task_h для n=2"
    assert [round(x, 5) for x in task_h(3)] == [1.0, 0.5, 0.83333], "Ошибка в task_h для n=3"

    # Тестирование функции task_i
    assert [round(x, 5) for x in task_i(1)] == [1.0], "Ошибка в task_i для n=1"
    assert [round(x, 5) for x in task_i(2)] == [1.0, 2.5], "Ошибка в task_i для n=2"
    assert [round(x, 5) for x in task_i(3)] == [1.0, 2.5, 4.66667], "Ошибка в task_i для n=3"

