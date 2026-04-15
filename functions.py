import os

def get_unique_path(path):
    base, ext = os.path.splitext(path)
    counter = 1

    new_path = path
    while os.path.exists(new_path):
        new_path = f"{base}_{counter}{ext}"
        counter += 1

    return new_path


