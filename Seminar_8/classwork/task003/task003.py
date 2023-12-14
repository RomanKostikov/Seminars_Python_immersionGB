# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import csv
import json


def save_to_csv():
    # Read the data from the file created in the previous task
    with open("C:/Users/roman/Desktop/Work for IT/GeekBrains/seminars/Python_immersion/Seminar_8/classwork/"
              "task002/result.json", "r") as file:
        data = json.load(file)

    # Extract the keys and values from the JSON data
    rows = []
    for access_level, users in data.items():
        for identifier, name in users.items():
            rows.append([access_level, identifier, name])

    # Write the data to a CSV file
    with open("output.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Access Level", "Identifier", "Name"])  # Write header row
        writer.writerows(rows)


save_to_csv()
