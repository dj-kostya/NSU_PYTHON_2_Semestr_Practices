#!/usr/bin/env python

"""

"""
import os


def cnt_files_in_folder(folder, formats):
    def is_true_ext(file):

        return not formats or os.path.splitext(file)[-1] in formats

    return sum([len(list(filter(is_true_ext, files))) for _, _, files in os.walk(folder)])
