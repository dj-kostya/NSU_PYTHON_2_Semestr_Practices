from lecture6 import DataLoader


def print_all_files(folder='.'):
    directory: DataLoader = DataLoader(folder)
    for path in directory.get_all_files_in_folder():
        print(path)


# print_all_files(folder='.') ->
# path\to\project\lecture6\dataloader.py
# path\to\project\lecture6\filename_validator.py
# path\to\project\lecture6\cnt_lines_in_files.py
# path\to\project\lecture6\print_all_files_in_folder.py
# path\to\project\lecture6\split.py
# path\to\project\lecture6\ReverseIter.py
# path\to\project\lecture6\__init__.py
# path\to\project\lecture6\wiki_articles\ml_frameworks\pytorch.txt
# path\to\project\lecture6\wiki_articles\ml_frameworks\tensorflow.txt
# path\to\project\lecture6\wiki_articles\programming_languages\compiled\c + +.pdf
# path\to\project\lecture6\wiki_articles\programming_languages\compiled\java.txt
# path\to\project\lecture6\wiki_articles\programming_languages\interpreted\python.txt
# path\to\project\lecture6\wiki_articles\programming_languages\interpreted\r.docx

