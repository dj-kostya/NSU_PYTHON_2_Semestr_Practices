#!/usr/bin/env python

"""
Data Processing Pipeline script - is aimed at miscellaneous data 
processing and performing various techniques for information extration.

Full description and code is still under development and construction.

TODO: complete module docstring after completion of basic functionality.
"""

import os
import re
from pathlib import Path

from Practice6 import DataLoader

# TODO: remove constant variables and make arguments parsing
# ( will do together on the next classes )
DIR_PATH = Path("wiki_articles/").absolute()
FORMATS = ['.txt', '.pdf', '.docx']
SAVE_DIR_PATH = Path("wiki_articles_processed/")


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


def saving_data(processed_lines, relative_path_of_file):
    """
    Function for saving data in original tree
    :param processed_lines:
    :param relative_path_of_file: path to save
    :return: None
    """
    # TODO: make files saving with the same relative paths structure
    # ( right now all files will be saved in one dir, structure is lost )
    file_path = os.path.join(SAVE_DIR_PATH, relative_path_of_file)
    make_directory(file_path)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(processed_lines)


# endregion


if __name__ == '__main__':
    data_loader = DataLoader(DIR_PATH, formats=FORMATS)
    # TODO: add a process visualization for more information
    # ( will do together on the next classes )
    for file_name, lines, depth in data_loader.folder_walk():
        relative_path = os.path.relpath(file_name, str(DIR_PATH))
        processed_data = processing(lines)
        name, ext = os.path.splitext(relative_path)
        saving_data(processed_lines=processed_data, relative_path_of_file=f'{name}.txt')
