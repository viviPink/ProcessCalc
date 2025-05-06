#include <iostream>
#include <vector>
#include <omp.h>     // Подключаем библиотеку OpenMP для параллельного программирования
#include <cstdlib>   
#include <ctime>     
#include <chrono>    // Для измерения времени выполнения

using namespace std;
using namespace chrono;
extern void Tests2();

//set OMP_NUM_THREADS = 4     # Для Windows
//g++ -fopenmp program.cpp -o program2


// Функция для заполнения вектора случайными числами
void fillRandom(vector<size_t>& vec) {
    for (size_t& num : vec) {
        num = rand() % 100 + 1; // Генерация чисел от 1 до 100
    }
}

// Функция для вычисления скалярного произведения (последовательно)
size_t scalarProductSequential(const vector<size_t>& A, const vector<size_t>& B) {
    int scalar = 0;
    for (size_t i = 0; i < A.size(); ++i) {
        scalar += A[i] * B[i];
    }
    return scalar;
}

// Функция для вычисления скалярного произведения (параллельно)
size_t scalarProductParallel(const vector<size_t>& A, const vector<size_t>& B) {
    size_t scalar = 0;
#pragma omp parallel for reduction(+:scalar)
    for (size_t i = 0; i < A.size(); ++i) {
        scalar += A[i] * B[i];
    }
    return scalar;
}

int main() {
    Tests2();
    size_t n; // Переменная для хранения размера векторов

    // Запрашиваем у пользователя размер векторов
    cout << "vector size: ";
    cin >> n;

    // Создаем два вектора A и B для хранения элементов
    vector<size_t> A(n), B(n);

    // Инициализация генератора случайных чисел
    srand(static_cast<unsigned>(time(0)));

    // Заполняем векторы случайными числами
    fillRandom(A);
    fillRandom(B);

    //// Выводим сгенерированные векторы
    //cout << "A: ";
    //for (int num : A) {
    //    cout << num << " ";
    //}
    //cout << endl;

    //cout << "B: ";
    //for (int num : B) {
    //    cout << num << " ";
    //}
    //cout << endl;

    // Вычисляем скалярное произведение последовательно
    auto start_seq = high_resolution_clock::now(); // Начало измерения времени
    size_t scalar_seq = scalarProductSequential(A, B);
    auto end_seq = high_resolution_clock::now(); // Конец измерения времени
    auto duration_seq = duration_cast<microseconds>(end_seq - start_seq).count();

    // Вычисляем скалярное произведение параллельно
    auto start_par = high_resolution_clock::now(); // Начало измерения времени
    size_t scalar_par = scalarProductParallel(A, B);
    auto end_par = high_resolution_clock::now(); // Конец измерения времени
    auto duration_par = duration_cast<microseconds>(end_par - start_par).count();

    // Выводим результаты
    cout << "result (sequential): " << scalar_seq << endl;
    cout << "time (sequential): " << duration_seq << " мкс" << endl;

    cout << "result (parallel): " << scalar_par << endl;
    cout << "time (parallel): " << duration_par << " мкс" << endl;

    cout << "threads: " << omp_get_max_threads() << endl;
}