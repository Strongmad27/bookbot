def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

from stats import word_count
from stats import letter_counter

def main():
    path_to_file = "books/frankenstein.txt"
    book_string = get_book_text(path_to_file)
    count = word_count(book_string)
    letters = letter_counter(book_string)  
    print(f"{count} words found in the document")
    print(letters)

main()