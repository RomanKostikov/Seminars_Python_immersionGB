# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json
import hashlib


def process_csv(input_file, output_file):
    # Read the data from the CSV file
    with open(input_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header row
        rows = list(reader)

    # Process the rows
    processed_rows = []
    for row in rows:
        # Complete the ID to 10 digits with leading zeros
        row[1] = row[1].zfill(10)

        # Make the first letter of each name uppercase
        row[2] = row[2].capitalize()

        # Compute the hash based on the name and identifier
        hash_value = hashlib.sha256((row[2] + row[1]).encode()).hexdigest()
        row.append(hash_value)

        # Create a dictionary for the processed row
        processed_row = dict(zip(headers, row))
        processed_rows.append(processed_row)

    # Save the processed rows to a JSON file
    with open(output_file, "w") as jsonfile:
        json.dump(processed_rows, jsonfile, indent=4)


process_csv("C:/Users/roman/Desktop/Work for IT/GeekBrains/seminars/Python_immersion/Seminar_8/classwork/"
            "task003/output.csv", "output.json")
