import os


def change_extension(file_path, new_extension):
    base_name, _ = os.path.splitext(file_path)
    new_file_path = base_name + "." + new_extension
    os.rename(file_path, new_file_path)


# Example usage:
change_extension("C:/Users/Swadesh Sharma/Downloads/Telegram Desktop/abc.001", "zip")
print("Successfully Changed!")