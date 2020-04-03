from os.path import splitext, join
from os import walk
from pathlib import Path


class DataLoader:
    """
    Class that use for working with files and folders
    """
    def __init__(self, filename):
        self.path: Path = Path(filename)
        self.exist: bool = self.path.exists()
        self.stringify: str = str(self.path)
        if not self.exist:
            return
        self.is_file: bool = self.path.is_file()
        self.is_dir: bool = self.path.is_dir()
        if self.is_file:
            name, ext = splitext(self.stringify)
            self.filename: str = name
            self.extension: str = ext

    def _validate_read_file(self, formats):
        """
        Validate file to reading
        :param formats: use it to validate format of file
        """
        if not self.exist:
            raise FileNotFoundError(f"{self.stringify} not exist")
        if not self.is_file:
            raise ValueError(f"{self.stringify} is not a file")
        if not formats:
            return
        if self.extension not in formats:
            raise ValueError(f"{self.stringify} has invalid format")

    def _validate_read_dir(self):
        """
        Validate folder to reading
        """
        if not self.is_dir:
            raise ValueError(f"{self.stringify} is not a folder")
        if not self.exist:
            raise FileNotFoundError(f"{self.stringify} not exist")

    def _validate_write_file(self):
        """
        Validate file to writing
        """
        if self.exist:
            raise FileExistsError(f"{self.stringify} already exist")

    def readline_from_file(self, formats=None):
        """
        :param formats: use it to validate format of file
        :return: generator expression, which return all lines in file
        """
        self._validate_read_file(formats)
        with open(self.stringify, 'r') as f:
            while True:
                line = f.readline()
                if line == '':
                    break
                yield line

    def partition_read_lines_of_file(self, particle_len: int):
        """
        Partition file reading
        :param particle_len: len of partition
        :return: generator expression, which return list of lines of a file whose less than or equal particle_len
        """
        new_list = []
        lines = iter(self.readline_from_file())
        try:
            while True:
                new_list.append(next(lines))
                if not len(new_list) % particle_len:
                    yield new_list
                    new_list.clear()
        except StopIteration:
            if new_list:
                yield new_list

    def write_file(self, lines: list):
        """
        Write lines to file
        :param lines: lines for writing
        """
        self._validate_write_file()
        with open(self.stringify, 'w') as f:
            f.writelines(lines)

    def get_all_files_in_folder(self):
        """
        :return:  generator expression, which return DataLoader object of all files in folder
        """
        self._validate_read_dir()
        for root, dirs, files in walk(self.stringify):
            for file in files:
                yield DataLoader(join(root, file))

    def get_stringify_path(self):
        return self.stringify

    def get_abs_path(self):
        return self.path.absolute()

    def get_str_abs_path(self):
        return str(self.get_abs_path())

    def is_cur_ext(self, formats) -> bool:
        return formats and self.extension in formats

    def __str__(self):
        return self.get_str_abs_path()
