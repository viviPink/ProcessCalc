using System;
using System.Collections.Concurrent; // Для потокобезопасной коллекции
using System.Diagnostics;            // Для измерения времени выполнения
using System.Threading;              

namespace th_pool
{
    class Program
    {
        // Глобальная переменная для хранения счетчика
        private static int totalCount = 0;

        // Объект для синхронизации доступа к totalCount
        private static readonly object countLock = new object();

        /*
         * - totalCount является общей переменной для всех потоков.
         * - Она должна быть статической, чтобы быть доступной в методах, вызываемых из разных потоков
         * 
         * readonly
         * - countLock используется только для синхронизации. Он инициализируется один раз при запуске программы и не должен изменяться.
         */

        // Функция для подсчета элементов
        private static void CountElements(int[] array, int start, int end, int threshold)
        {
            int partialCount = 0;

            // Проходим по подмассиву от start до end
            for (int i = start; i < end; i++)
            {
                if (array[i] > threshold)
                {
                    partialCount++; // Увеличиваем счетчик, если элемент больше порогового значения
                }
            }

            // Защищаем доступ к общей переменной totalCount с помощью lock
            lock (countLock)
            {
                /*
                 * - Когда несколько потоков одновременно пытаются изменить totalCount, может возникнуть гонка данных 
                 * - Lock гарантирует, что только один поток может изменять totalCount в любой момент времени
                 */
                totalCount += partialCount;
            }
        }

        static void Main(string[] args)
        {
            Console.Write("Введите размер массива (n): ");
            int n = int.Parse(Console.ReadLine());

            // Создаем массив и заполняем его случайными числами
            int[] array = new int[n];
            Random random = new Random();
            for (int i = 0; i < n; i++)
            {
                array[i] = random.Next(1, 100); // Генерация случайных чисел от 1 до 99
            }

            // Выводим массив на экран
            Console.WriteLine("Массив заполнен случайными числами:");
            Console.WriteLine(string.Join(", ", array));

            Console.Write("Введите пороговое значение (X): ");
            int threshold = int.Parse(Console.ReadLine());

            // Environment.ProcessorCount возвращает количество ядер процессора
            int numThreads = Environment.ProcessorCount;

            // Создаем пул потоков с количеством потоков, равным количеству ядер процессора
            ThreadPool pool = new ThreadPool(numThreads);

            // Как работает разделение массива на части?
            // Массив делится на numThreads частей. Каждая часть обрабатывается одним потоком.
            // Размер каждой части вычисляется как chunkSize = n / numThreads.
            int chunkSize = n / numThreads;

            // Создаем объект Stopwatch для измерения времени выполнения
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            // Разделяем массив на части и добавляем задачи в пул
            for (int i = 0; i < numThreads; i++)
            {
                int start = i * chunkSize; // Начальный индекс части массива
                int end = (i == numThreads - 1) ? n : start + chunkSize; // Конечный индекс части массива

                // Лямбда-выражение позволяет передать анонимную функцию в метод Enqueue
                // В данном случае мы передаем функцию CountElements с параметрами start, end и threshold
                pool.Enqueue(() => CountElements(array, start, end, threshold));
            }

            // GC.Collect() принудительно вызывает сборщик мусора
            // Это нужно для того, чтобы деструктор (~ThreadPool) был вызван и все потоки завершили свою работу
            GC.Collect();

            // Останавливаем таймер
            stopwatch.Stop();

            // Выводим результат
            Console.WriteLine($"Количество элементов, больших {threshold}: {totalCount}");
            Console.WriteLine($"Время выполнения: {stopwatch.ElapsedMilliseconds} мс");
        }
    }
}