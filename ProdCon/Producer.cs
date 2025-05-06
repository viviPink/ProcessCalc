using System;
using System.Collections.Concurrent;
using System.IO;

namespace ProducerConsumerApp
{
    public class Producer
    {
        /// <summary>
        /// Добавляет файлы из указанной папки в очередь.
        /// </summary>
        /// <param name="folderPath">Путь к папке с текстовыми файлами</param>
        /// <param name="fileQueue">Очередь для хранения путей к файлам</param>
        public static void ProduceFiles(string folderPath, BlockingCollection<string> fileQueue)
        {
            try
            {
                // Получаем все файлы с расширением .txt в указанной папке
                var files = Directory.GetFiles(folderPath, "*.txt");

                foreach (var file in files)
                {
                    fileQueue.Add(file); // Добавляем файл в очередь
                    Console.WriteLine($"Добавлен файл: {Path.GetFileName(file)}");
                }
            }
            catch (DirectoryNotFoundException)
            {
                Console.WriteLine($"Папки '{folderPath}' нет.");
            }

            // Сигнализируем о завершении добавления файлов
            fileQueue.CompleteAdding();
        }
    }
}