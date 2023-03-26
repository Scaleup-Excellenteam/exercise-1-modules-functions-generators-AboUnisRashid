import os


def get_path(path):
    files = []
    for file in os.listdir(path):
        if file.startswith("deep"):
            files.append(file)
    return files



