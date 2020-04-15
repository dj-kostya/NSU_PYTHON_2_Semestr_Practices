#!/usr/bin/env python
"""
Data Processing Pipeline script - is aimed at miscellaneous data
processing and performing various techniques for information extration.

Full description and code is still under development and construction.

TODO: complete module docstring after completion of basic functionality.
"""

import argparse
import os
import re
from pathlib import Path

from utls import aux_function
from src.data_loader import DataLoader
from tqdm import tqdm


def load_args():
    arg_parse = argparse.ArgumentParser(description="Load arguments")
    arg_parse.add_argument("-f", "--formats", type=str, required=False,
                           help="Formats of files to processing. Splited by ,")
    arg_parse.add_argument("-d", "--depth", type=int, required=False, default=None,
                           help="Max depth of file structure")
    arg_parse.add_argument("--raw-data-output", type=str, required=False, default='raw_data.txt',
                           help="Filename for raw lines file.")
    arg_parse.add_argument("input_directory", metavar='input_directory', type=str, default='./',
                           help='Path to the directory containing file for processing', nargs='+')
    arg_parse.add_argument("-od", "--output-directory", type=str, required=True,
                           help='Path to the directory to save processing files')
    return arg_parse.parse_args()


# region AUXILIARY FUNCTIONS
def make_directory(file_path):
    """Checks if a directory for specified file exists and creates
    it if not.

    Parameters
    ----------
    file_path : str
        Path to the file to check for parent directory existence

    Returns
    -------
    None
    """
    directory = Path(file_path).parent
    if not os.path.isdir(directory):
        os.makedirs(directory)


def processing(lines_of_file):
    """
    Processing lines of files
    :param lines_of_file:
    :return: processed lines of file
    """
    processed_lines = []
    for line in lines_of_file:
        line = line.strip()
        regex = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
        sentences = re.split(regex, line)
        processed_lines.extend([sent + '\n' for sent in sentences])
    return processed_lines


def saving_data_with_saving_tree(processed_lines, relative_path_of_file, encoding='utf-8'):
    """
    Function for saving data in original tree
    :param processed_lines:
    :param relative_path_of_file: path to save
    :param encoding: encoding for output file
    :return: None
    """
    file_path = os.path.join(SAVE_DIR_PATH, relative_path_of_file)
    make_directory(file_path)
    with open(file_path, 'w', encoding=encoding) as f:
        f.writelines(processed_lines)


def append_data_to_file(processed_lines, file_path, encoding='utf-8'):
    """
    Function for saving data in one file
    :param processed_lines:
    :param file_path: path to file for appending
    :param encoding: encoding for output file
    :return: None
    """
    make_directory(file_path)
    with open(file_path, 'a', encoding=encoding) as f:
        f.writelines(processed_lines)


# endregion


if __name__ == '__main__':

    # region PARSE ARGS
    args = load_args()
    DIR_PATH = args.input_directory[0]
    DEPTH = args.depth
    RAW_DATA_FILENAME = args.raw_data_output
    DIR_PATH = Path(DIR_PATH).absolute()
    SAVE_DIR_PATH = Path(args.output_directory).absolute()
    try:
        FORMATS = list(map(str.strip, args.formats.split(',')))
    except AttributeError as e:
        FORMATS = None
    # endregion

    data_loader = DataLoader(DIR_PATH, formats=FORMATS)
    cnt_file = aux_function.cnt_files_in_folder(data_loader.get_stringify_path(), formats=FORMATS)
    for file_name, lines, depth in tqdm(data_loader.folder_walk(), total=cnt_file, desc='Progress'):
        relative_path = os.path.relpath(file_name, str(DIR_PATH))
        processed_data = processing(lines)
        name, ext = os.path.splitext(relative_path)
        if not DEPTH or depth < DEPTH:
            saving_data_with_saving_tree(processed_lines=processed_data, relative_path_of_file=f'{name}.txt')
        else:
            append_data_to_file(processed_lines=processed_data,
                                file_path=os.path.join(SAVE_DIR_PATH, RAW_DATA_FILENAME))
