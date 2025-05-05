import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

from stats import word_count
from stats import letter_counter
from stats import sorter

def main():
    path_to_file = sys.argv[1]
    book_string = get_book_text(path_to_file)
    count = word_count(book_string)
    letters = letter_counter(book_string)
    let_list = sorter(letters)  
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for let_dic in let_list:
        char = let_dic["char"]
        num = let_dic["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
main()