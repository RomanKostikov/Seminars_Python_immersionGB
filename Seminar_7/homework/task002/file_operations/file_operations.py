import os


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
