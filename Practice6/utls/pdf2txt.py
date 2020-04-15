"""Script for simple text data parsing from PDF files.
Uses PDFMiner module, for more information please refer to:

Docs: https://pdfminersix.readthedocs.io/en/latest/
GitHub: https://github.com/pdfminer/pdfminer.six

Script contains a function for transforming a PDF file into
text data. Returns raw text (in one string) extracted from the PDF file.
Raw text comes with 'b' literal, so needs to be decoded with str.decode("utf-8").

NOTE: As PDFMiner is a simple parser, results are not guaranteed to be well-formed.
It is recommended to use advanced parsing techniques and tools.
Additionally, this parser can process only text data.
"""

from io import BytesIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage


def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)

    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    filepath.close()
    device.close()
    retstr.close()
    return text
