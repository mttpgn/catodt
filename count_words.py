#!/usr/bin/env python3

import os
import sys
from odf import text, teletype
from odf.opendocument import load


def countAllWords(directory):
    files = sorted(os.listdir(directory))
    total_word_count = 0
    for file in files:
        if file.endswith('.odt'):
            file_path = os.path.join(directory, file)
            doc = load(file_path)
            word_count = 0
            # Extract text from each paragraph element
            for paragraph in doc.getElementsByType(text.P):
                word_count += len(teletype.extractText(paragraph).split())
            print(f"Length of {file}: {word_count} words.")
            total_word_count += word_count
    print(f"Total length of all files: {total_word_count} words.")
    return total_word_count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: count_words.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    countAllWords(directory)
