#!/usr/bin/python3
import sys

from pathlib import Path

from stats import (
    count_words,
    count_characters,
    order_dicts
)

def get_book_text(file_path:Path) -> str:
    """
    Gets a file_path and returns its content as a string
    """
    with open(file_path, "+r", encoding="utf-8") as f:
        output = f.read()
    return output

if __name__=="__main__":
    if len(sys.argv) >1:
        f_path = Path.cwd() / sys.argv[1]
        text = get_book_text(f_path)
        print(f"Analyzing book found at {f_path}")
        print("----------- Word Count ----------")
        n_words = count_words(text)
        print(f"Found {n_words} total words")
        print("--------- Character Count -------")
        ch_dict = count_characters(text)
        ls_dict = order_dicts(ch_dict)
        for dic in ls_dict:
            print(f"{dic['char']}: {dic['value']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
