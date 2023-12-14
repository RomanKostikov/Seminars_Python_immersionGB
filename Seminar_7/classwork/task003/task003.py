# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

# def multiply_numbers(file1, file2, output_file):
#     with (open(file1, 'r', encoding='UTF-8') as f1, open(file2, 'r', encoding='UTF-8') as f2,
#           open(output_file, 'w', encoding='UTF-8') as f_out):
#         lines1 = f1.readlines()
#         lines2 = f2.readlines()
#         for i in range(min(len(lines1), len(lines2))):
#             try:
#                 num1 = float(lines1[i].split()[0].split('|')[0])
#                 num2 = float(lines2[i].split()[0].split('|')[0])
#                 product = num1 * num2
#                 name = lines1[i].split()[1]
#                 if product < 0:
#                     f_out.write(f"{name.lower()} {int(abs(product))}\n")
#                 else:
#                     f_out.write(f"{name.upper()} {int(product)}\n")
#             except ValueError:
#                 print(f"Error: could not convert string to float: {lines1[i].split()[0]}")
#
#
# multiply_numbers('myfile.txt', 'names.txt',
#                  'output_file.txt')

# Решение на семинаре
def func():
    with (open('names.txt', 'r', encoding='UTF-8') as file_name,
          open('example.txt', 'r', encoding='UTF-8') as file_nums):
        data_names = file_name.readlines()
        data_nums = file_nums.readlines()

    data_names = list(map(lambda x: x.strip(), data_names))
    data_nums = [tuple(map(float, item.strip().split(' | '))) for item in data_nums]
    data_nums = [item[0]*item[1] for item in data_nums]
    max_len = max([len(data_names), len(data_nums)])
    result = []
    for i in range(max_len):
        row = ''
        if data_nums[i] < 0:
            row = f'{data_names[i].lower()} | {abs(data_nums[i])}'
        else:
            row = f'{data_names[i].upper()} | {round(data_nums[i],0)}'
        result.append(row)
    with open('result.txt', 'w', encoding='UTF-8') as file:
        file.write('\n'.join(result))


func()
