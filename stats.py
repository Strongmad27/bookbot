def word_count(book_string):
    word_list = book_string.split()
    count = len(word_list)
    return count

def letter_counter(book_string):
    word_list = book_string.lower()
    letter_count = {}
    for letter in word_list:
        if letter in letter_count:
            letter_count[letter]+=1
        else:
            letter_count[letter] = 1
    return letter_count

def sorter(letters):
    letters_list = []
    for letter, count in letters.items():
        letters_list.append({"char": letter, "num": count})
    def sort_on(dict):
        return dict["num"]
    letters_list.sort(reverse=True, key=sort_on)
    return letters_list


