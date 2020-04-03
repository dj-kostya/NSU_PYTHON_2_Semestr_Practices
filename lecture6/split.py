from sys import argv

from lecture6 import DataLoader


def file_splitter(file, cnt_line):
    try:
        cnt_line = int(cnt_line)
    except ValueError:
        raise ValueError("Not a number")
    file = DataLoader(file)
    for idx, lines in enumerate(file.partition_read_lines_of_file(particle_len=cnt_line)):
        new_file = DataLoader(f'{idx + 1}_file_{file.path.name}')
        new_file.write_file(lines)


if __name__ == '__main__':
    if len(argv) != 3:
        raise ValueError("Not valid arguments!")
    file_splitter(argv[2], argv[1])  # make a lot of files with names like {some_index}_file_{argv[2]}
