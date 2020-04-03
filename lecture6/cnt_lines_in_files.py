from lecture6 import DataLoader


def validate_line(line: str):
    if len(line) == 0:
        return False
    try:
        if line.strip()[0] == '#':
            return False
    except IndexError:
        return False
    return True


def cnt_all_lines(folder, formats=('.py',)):
    directory = DataLoader(folder)
    cur_sum = 0
    for file in directory.get_all_files_in_folder():
        if not file.is_cur_ext(formats):
            continue
        cur_sum += sum(map(validate_line, file.readline_from_file(formats=None)))
    return cur_sum


# if __name__ == '__main__':
#     print(cnt_all_lines('.', formats=('.txt',))) -> 15
#     print(cnt_all_lines('.')) -> 139
