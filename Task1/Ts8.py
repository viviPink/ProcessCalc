import numpy as np
from operationFirst import calculate_matrix



def main():
    print("Выберите способ ввода матрицы:")
    ch = input("1 - Ввести матрицу вручную\n2 - Использовать баз матрицу\n ")

    if ch== "1":
        # Ввод матрицы вручную
        try:
            n = int(input("Введите размер квадратной матрицы (n x n): "))
            A = []
            print(f"Введите {n} строк по {n} ")
            for _ in range(n):
                row = list(map(float, input().split()))
                if len(row) != n:
                    raise ValueError("Количество элементов в строке не соответствует размеру матрицы.")
                A.append(row)
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            return
    elif ch == "2":
        A = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        print("Используется базовая матрица:")
        print(np.array(A))
    else:
        print("что-то пошло не так, перезвоните позже")
        return

    B = calculate_matrix(A)

    print("\nРезультат (матрица B):")
    print(B)



if __name__ == "__main__":
    main()
