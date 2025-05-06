#include <iostream>
#include <vector>
#include <omp.h>     // Подключаем библиотеку OpenMP для параллельного программирования
#include <chrono>    // Для измерения времени выполнения
#include <cstdlib>   // Для std::rand и std::srand
#include <ctime>     // Для std::time

using namespace std;
using namespace chrono;
extern void runTests();

// Функция для последовательного подсчета
size_t countSequential(const vector<size_t>& sequence) {
    size_t count = 0;
    for (size_t num : sequence) {
        if (num % 3 == 0 && num % 5 != 0) {
            count++;
        }
    }
    return count;
}

// Функция для параллельного подсчета
size_t countParallel(const vector<size_t>& sequence) {
    int count = 0;
#pragma omp parallel for reduction(+:count)
    for (size_t i = 0; i < sequence.size(); ++i) {
        if (sequence[i] % 3 == 0 && sequence[i] % 5 != 0) {
            count++;
        }
    }
    return count;
}

int main() {
    runTests();
    size_t n; // Переменная для хранения размера последовательности

    // Ввод размера последовательности
    cout << "N: ";
    cin >> n;

    // Создаем динамический массив (вектор) для хранения последовательности чисел
    vector<size_t> sequence(n);

    // Инициализация генератора случайных чисел
    srand(static_cast<unsigned>(time(0))); // Инициализация на основе текущего времени

    // Заполнение массива случайными числами
    for (size_t i = 0; i < n; ++i) {
        sequence[i] = rand() % 100 + 1; // Генерация чисел от 1 до 100
    }

    // Вывод сгенерированной последовательности
   /* cout << "numbers: ";
    for (size_t num : sequence) {
        cout << num << " ";
    }
    cout << endl;*/

    // Последовательная версия подсчета
    auto start_seq = high_resolution_clock::now(); // Начало измерения времени
    size_t count_seq = countSequential(sequence);
    auto end_seq = high_resolution_clock::now(); // Конец измерения времени
    auto time_seq = duration_cast<microseconds>(end_seq - start_seq).count();

    // Параллельная версия подсчета
    auto start_par = high_resolution_clock::now(); // Начало измерения времени
    size_t count_par = countParallel(sequence);
    auto end_par = high_resolution_clock::now(); // Конец измерения времени
    auto time_par = duration_cast<microseconds>(end_par - start_par).count();

    // Вывод результатов
    cout << "numbers /3 not /5 (sequential): " << count_seq << endl;
    cout << "time (sequential): " << time_seq << " мкс" << endl;

    cout << "numbers /3 not /5 (parallel): " << count_par << endl;
    cout << "time (parallel): " << time_par << " mks" << endl;

    cout << "threads: " << omp_get_max_threads() << endl;

    return 0;
}