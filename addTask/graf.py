import time
import numpy as np
import torch

# Размер матриц
size = 12000

# Количество повторений для замера времени
rep = 5


# Создание матриц в NumPy
np_matrix_a = np.random.rand(size, size).astype(np.float32)
np_matrix_b = np.random.rand(size, size).astype(np.float32)
# Создание матриц
matrix_a = [[i + j for j in range(size)] for i in range(size)]
matrix_b = [[i - j for j in range(size)] for i in range(size)]
np_matrix_a = np.array(matrix_a)
np_matrix_b = np.array(matrix_b)




"""Это функция из библиотеки PyTorch, которая создает новый тензор на основе входных данных.
Тензор — это многомерный массив, аналогичный массивам NumPy, но с дополнительными возможностями, такими как поддержка GPU и автоматическое дифференцирование.
"""
torch_matrix_a_cpu = torch.tensor(np_matrix_a, dtype=torch.float32)
torch_matrix_b_cpu = torch.tensor(np_matrix_b, dtype=torch.float32)

# перемещают тензоры (или матрицы) с CPU на GPU.
if torch.cuda.is_available():
    torch_matrix_a_gpu = torch_matrix_a_cpu.to('cuda')
    torch_matrix_b_gpu = torch_matrix_b_cpu.to('cuda')


    # Функция для перемножения матриц как списков
    def multiply_lists(matrix_a, matrix_b):
        result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
        for i in range(len(matrix_a)):
            for j in range(len(matrix_b[0])):
                for k in range(len(matrix_b)):
                    result[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return result


    # Замеры времени для списков Python
    def m_python():
        times = []
        for _ in range(rep):
            start_time = time.time()
            multiply_lists(matrix_a, matrix_b)
            end_time = time.time()
            times.append(end_time - start_time)
        return sum(times) / len(times)


    # Замеры времени для NumPy
    def m_numpy():
        times = []
        for _ in range(rep):
            start_time = time.time()

            np.dot(np_matrix_a, np_matrix_b)

            end_time = time.time()
            times.append(end_time - start_time)
        return sum(times) / len(times)


    # Замеры времени для PyTorch на CPU
    def m_torch_cpu():
        times = []
        for _ in range(rep):
            start_time = time.time()

            torch.matmul(torch_matrix_a_cpu, torch_matrix_b_cpu)

            end_time = time.time()
            times.append(end_time - start_time)
        return sum(times) / len(times)


    # Замеры для PyTorch на GPU
    torch_gpu_time = m_torch_gpu()
    print(f"PyTorch GPU: {torch_gpu_time:.8f}")

# Замеры времени для PyTorch на GPU
def m_torch_gpu():
    if not torch.cuda.is_available():
        print("штуку через среду выполнения нужно включить")
        return None

    times = []
    for _ in range(rep):
        start_time = time.time()

        # Выполняем операцию на GPU
        torch.matmul(torch_matrix_a_gpu, torch_matrix_b_gpu)


        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)


# Замеры для PyTorch на GPU
torch_gpu_time = m_torch_gpu()

print(f"PyTorch GPU: {torch_gpu_time:.8f}")

# Замеры для списков Python
python_time = m_python()
print(f"Python lists: {python_time:.2f} ")
# Замеры для NumPy
numpy_time = m_numpy()
print(f"NumPy arrays: {numpy_time:.2f} ")

# Замеры для PyTorch на CPU
torch_cpu_time = m_torch_cpu()
print(f"PyTorch CPU: {torch_cpu_time:.8f} ")