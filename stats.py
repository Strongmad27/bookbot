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
    for letter in letter_count:
        
    return letter_count


