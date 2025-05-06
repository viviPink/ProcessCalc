#include <cassert>
#include <vector>
#include <iostream>

// ���������� ������� �� ��������� �����
extern size_t countSequential(const std::vector<size_t>& sequence);
extern size_t countParallel(const std::vector<size_t>& sequence);

// ������� ��� ������� ������
void runTests() {
  
    {
        std::vector<size_t> sequence = { 45, 78, 23, 67, 89, 12 };
        assert(countSequential(sequence) == 2);
        assert(countParallel(sequence) == 2);
    }

    //  ������ ������
    {
        std::vector<size_t> sequence = {};
        assert(countSequential(sequence) == 0);
        assert(countParallel(sequence) == 0);
    }
    {
        std::vector<size_t> sequence = { 5, 10, 20, 25 };
        assert(countSequential(sequence) == 0);
        assert(countParallel(sequence) == 0);
    }

    {
        std::vector<size_t> sequence = { 3 };
        assert(countSequential(sequence) == 1);
        assert(countParallel(sequence) == 1);
    }


    {
        std::vector<size_t> sequence = { 3, 9, 18, 21 };
        assert(countSequential(sequence) == 4);
        assert(countParallel(sequence) == 4);
    }

    std::cout << "good test" << std::endl;
}

