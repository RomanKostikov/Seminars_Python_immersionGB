# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории
# На входе:
# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
# На выходе:
# (new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc,
#  new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc)
import os
import shutil

# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)

# Заполнить тестовую папку
for i in range(10):
    file_name = f"test{i}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

file_name = "test.doc"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()


def rename_files(desired_name, num_digits, source_ext, target_ext):
    # Get the list of files in the test_folder directory
    files = os.listdir("test_folder")

    # Sort the files to ensure consistent order
    files.sort()

    # Initialize a counter for the new file names
    counter = 1

    # Iterate over each file in the directory
    for file in files:
        # Check if the file has the specified source extension
        if file.endswith(source_ext):
            # Create the new file name with the desired name and the counter
            new_file_name = f"{desired_name}{str(counter).zfill(num_digits)}.{target_ext}"

            # Rename the file
            os.rename(os.path.join("test_folder", file), os.path.join("test_folder", new_file_name))

            # Increment the counter
            counter += 1


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

folder_content = ""
files = os.listdir(folder_path)
separator = ", "
files_as_string = separator.join(files)
print(files_as_string)

shutil.rmtree(folder_path)

# Ожидаемый ответ:
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc
# Ваш ответ:
# new_file_008.doc, test.doc, new_file_011.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc
