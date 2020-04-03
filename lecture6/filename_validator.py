from sys import argv


def get_valid_names(filenames: list):
    for _filename in filenames:
        if len(_filename) > 40:
            yield _filename


if __name__ == '__main__':
    if len(argv) in (0, 1):
        print("No arguments!")
    for filename in get_valid_names(argv[1:]):
        print(filename)
