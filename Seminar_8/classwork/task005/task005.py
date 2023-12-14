# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import os
import json
import pickle


def convert_json_to_pickle(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            json_file = os.path.join(directory, filename)
            pickle_file = os.path.join(directory, os.path.splitext(filename)[0] + ".pickle")

            with open(json_file, "r") as file:
                data = json.load(file)

            with open(pickle_file, "wb") as file:
                pickle.dump(data, file)


# Example usage
directory = "C:/Users/roman/Desktop/Work for IT/GeekBrains/seminars/Python_immersion/Seminar_8/classwork/task004"
convert_json_to_pickle(directory)
