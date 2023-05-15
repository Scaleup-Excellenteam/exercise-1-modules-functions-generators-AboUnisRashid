import os


def get_path(path):
    files = []
    for file in os.listdir(path):
        if file.startswith("deep"):
            files.append(file)
    return files


def main():
    get_path(input("please provide the path:"))
    return 0


if __name__ == '__main__':
    main()