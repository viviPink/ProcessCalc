#include <cassert>
#include <vector>
#include <iostream>

// Подключаем функции из основного файла
extern int scalarProductSequential(const std::vector<int>& A, const std::vector<int>& B);
extern int scalarProductParallel(const std::vector<int>& A, const std::vector<int>& B);


void Tests2() {
    
    {
        std::vector<int> A = { 1, 2, 3 };
        std::vector<int> B = { 4, 5, 6 };
        assert(scalarProductSequential(A, B) == 32);
        assert(scalarProductParallel(A, B) == 32);
    }

    {
        std::vector<int> A = {};
        std::vector<int> B = {};
        assert(scalarProductSequential(A, B) == 0);
        assert(scalarProductParallel(A, B) == 0);
    }
    {
        std::vector<int> A = { 0, 0, 0 };
        std::vector<int> B = { 1, 2, 3 };
        assert(scalarProductSequential(A, B) == 0);
        assert(scalarProductParallel(A, B) == 0);
    }
    {
        std::vector<int> A = { -1, -2, -3 };
        std::vector<int> B = { 4, 5, 6 };
        assert(scalarProductSequential(A, B) == -32);
        assert(scalarProductParallel(A, B) == -32);
    }

    // Тест 5: Проверка на больших векторах
    {
        std::vector<int> A(1'000'000, 2); // Массив из 1 миллиона элементов со значением 2
        std::vector<int> B(1'000'000, 3); // Массив из 1 миллиона элементов со значением 3
        assert(scalarProductSequential(A, B) == 6'000'000);
        assert(scalarProductParallel(A, B) == 6'000'000);
    }

    std::cout << "good tests" << std::endl;
}

