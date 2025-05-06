using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Diagnostics;            // Для измерения времени выполнения

namespace ProducerConsumerApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите путь к папке с текстовыми файлами: ");
            string folderPath = Console.ReadLine();

            // Создаем объект Stopwatch для измерения времени выполнения
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            // Создаем потокобезопасную очередь для файлов
            BlockingCollection<string> fileQueue = new BlockingCollection<string>();

            // Создаем словарь для хранения результатов
            Dictionary<string, int> results = new Dictionary<string, int>();

            // Запускаем Producer
            Producer.ProduceFiles(folderPath, fileQueue);

            // Запускаем Consumer
            Consumer.ConsumeFiles(fileQueue, results);

            // Останавливаем таймер
            stopwatch.Stop();

            // Выводим результаты
            Console.WriteLine("\nИтоговые результаты:");
            foreach (var result in results)
            {
                Console.WriteLine($"{result.Key}: {result.Value} слов");
                Console.WriteLine($"Время выполнения: {stopwatch.ElapsedMilliseconds} мс");
            }
        }
    }
}






//using System;
//using System.Collections.Concurrent;
//using System.IO;            // работа с путями       
//using System.Linq;
//using System.Threading;
//using System.Threading.Tasks;

////разбить на файлы  и путь к файлам добавить 
//// Реализует пример работы Producer-Consumer
//// продюсер помещает название файлов,которые нужно прочесть в очередь 
//// кон-ер считает количество слов в файле
//class ProducerConsumer
//{
//    static void Main(string[] args)
//    {
//        Console.WriteLine("подсчет количества слов в файле (берем 1 папку)");

//        // Очередь для задач (файлы для обработки)
//        // BlockingCollection - потокобезопасная коллекция (для предотвращения состояния гонки и тп)
//        var fileQueue = new BlockingCollection<string>();

//        // Общие результаты (словарь из строка+количество символов )
//        // ConcurrentDictionary гарантирует безопасность при многопоточной работе
//        var results = new ConcurrentDictionary<string, int>();

//        // Количество консумеров = количество ядер процессора(ProcessorCount)
//        // Используем все доступные процессорные ядра для максимальной параллелизации
//        // Environment.ProcessorCount- возращает количество логических процессоров, доступных в системе
//        int consumerCount = Environment.ProcessorCount;
//        Console.WriteLine($"количество работяг: {consumerCount}");

//        // Запуск консумеров
//        // Создаем массив Tas (по одному на каждого консумера)
//        // Task — это ключевая концепция для асинхронного и параллельного программирования
//        // Это абстракция, представляющая асинхронную операцию или единицу работы, которая может выполняться в фоновом режиме.
//        // Представляет асинхронную операцию - выполнение кода без блокировки основного потока
//        // Использует пул потоков - задачи выполняются в фоновых потоках из пула
//        // Поддерживает ожидание и продолжения - можно дожидаться завершения задачи или указать код, который выполнится после
//        // Позволяет получать результаты - через свойство Result или ключевое слово await
//        var consumers = new Task[consumerCount];
//        for (int i = 0; i < consumerCount; i++)
//        {
//            // Каждый Task выполняет метод ProcessFiles
//            // Task.Run автоматически запускает задачу в пуле потоков

//            //() => ProcessFiles(fileQueue, results)
//            //анонимная функция (лямбда, которая не принимает параметров 
//            //При вызове эта функция выполнит метод ProcessFiles 
//            //fileQueue - коллекция файлов
//            //results - словарь для результатов
//            consumers[i] = Task.Run(() => ProcessFiles(fileQueue, results));
//        }

//        // Producer - поиск файлов и добавление в очередь
//        string folderPath = "text_files"; // Папка с текстовыми файлами
//        try
//        {
//            // Получаем все файлы с расширением .txt в указанной папке
//            var files = Directory.GetFiles(folderPath, "*.txt");

//            // Добавляем каждый файл в очередь на обработку
//            foreach (var file in files)
//            {
//                fileQueue.Add(file); // Добавление в коллекцию файла
//                //берем только имя файла из полного пути
//                Console.WriteLine($"Добавлен файл: {Path.GetFileName(file)}");
//            }
//        }
//        catch (DirectoryNotFoundException)
//        {
//            Console.WriteLine($"Папки '{folderPath}' нет");
//            return;
//        }

//        // Сигнал конс-м о том что завершилось добавление элементов в очередб 
//        // После этого вызова консумер завершат работу, когда очередь станет пустой
//        fileQueue.CompleteAdding();

//        // Ожидание завершения всех консумеров
//        // Блокирует выполнение, пока все Task не завершатся
//        Task.WaitAll(consumers);

//        // Вывод результатов
//        // Сортируем по убыванию количества слов и выводим
//        Console.WriteLine("\nРезультата:");
//        //Метод OrderByDescending сортирует элементы коллекции по убыванию
//        foreach (var result in results.OrderByDescending(r => r.Value))
//        {
//            Console.WriteLine($"{result.Key}: {result.Value} слов");
//        }

//        Console.WriteLine("\nВсе!");
//    }


//    /// Метод консумера - обрабатывает файлы из очереди
//    /// queue  Очередь с файлами для обработки
//    /// results Словарь для сохранения результатов
//    static void ProcessFiles(BlockingCollection<string> queue, ConcurrentDictionary<string, int> results)
//    {

//        //Метод GetConsumingEnumerable() является частью класса BlockingCollection<T>
//        //используется для перечисления элементов коллекции в потокобезопасной манере
//        //Этот метод особенно полезен в многопоточных приложениях, где один или несколько
//        //потоков добавляют элементы в коллекцию, а другой поток (или потоки)
//        //извлекают и обрабатывают эти элементы

//        // Каждый раз, когда элемент извлекается через этот перечислитель, он удаляется из коллекции(потребляется)
//        //Если коллекция пуста, вызывающий поток блокируется, пока в коллекцию не будет добавлен новый элемент
//        foreach (var filePath in queue.GetConsumingEnumerable())
//        {
//            try
//            {
//                // Читаем весь текст файла
//                string text = File.ReadAllText(filePath);

//                // Подсчитываем количество слов
//                int wordCount = CountWords(text);

//                // Получаем только имя файла (без полного пути)
//                string fileName = Path.GetFileName(filePath);

//                // Добавляем результат в словарь
//                // TryAdd потокобезопасен и гарантирует атомарность операции
//                // Он пытается добавить пару ключ-значение в коллекцию
//                // и возвращает true, если добавление прошло успешно,
//                // или false, если ключ уже существует

//                results.TryAdd(fileName, wordCount);

//                Console.WriteLine($"Обработан: {fileName} ({wordCount} слов)");
//            }
//            catch (Exception ex)
//            {
//                Console.WriteLine($"Ошибка при обработке {filePath}: {ex.Message}");
//            }
//        }
//    }


//    /// Подсчитывает количество слов в тексте
//    // text -  Текст для анализа
//    // возращает количество слов
//    static int CountWords(string text)
//    {
//        // считаем слова, которые разделены символами 
//        char[] separators = new[] { ' ', '.', ',', ';', '!', '?', '\n' };

//        // Разбиваем текст на подстроки, используя указанные разделители
//        // StringSplitOptions.RemoveEmptyEntries - игнорирует пустые строки

//        //Метод Split разделяет строку на массив подстрок, используя указанные разделители
//        //Параметр StringSplitOptions.RemoveEmptyEntries удаляет из результата все пустые строки
//        // Свойство Length возвращает количество элементов в массиве
//        return text.Split(separators, StringSplitOptions.RemoveEmptyEntries).Length;
//    }
//}