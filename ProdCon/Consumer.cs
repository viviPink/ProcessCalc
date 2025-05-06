using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.IO;

namespace ProducerConsumerApp
{
    public class Consumer
    {
        /// <summary>
        /// Обрабатывает файлы из очереди.
        /// </summary>
        /// <param name="fileQueue">Очередь с файлами для обработки</param>
        /// <param name="results">Словарь для сохранения результатов</param>
        public static void ConsumeFiles(BlockingCollection<string> fileQueue, IDictionary<string, int> results)
        {
            foreach (var filePath in fileQueue.GetConsumingEnumerable())
            {
                try
                {
                    // Читаем текст из файла
                    string text = File.ReadAllText(filePath);

                    // Подсчитываем количество слов
                    int wordCount = CountWords(text);

                    // Сохраняем результат в словаре
                    string fileName = Path.GetFileName(filePath);
                    results[fileName] = wordCount;

                    Console.WriteLine($"Обработан: {fileName} ({wordCount} слов)");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Ошибка при обработке {filePath}: {ex.Message}");
                }
            }
        }

        /// <summary>
        /// Подсчитывает количество слов в тексте.
        /// </summary>
        /// <param name="text">Текст для подсчета слов</param>
        /// <returns>Количество слов в тексте</returns>
        private static int CountWords(string text)
        {
            char[] separators = new[] { ' ', '.', ',', ';', '!', '?', '\n' };

            // Разделяем строку на слова
            return text.Split(separators, StringSplitOptions.RemoveEmptyEntries).Length;
        }
    }
}