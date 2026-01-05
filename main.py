import sys
from stats import get_num_words, character_counter, dict_sorter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        
    file_contents = get_book_text(file_path)
    num_words = get_num_words(file_contents)
    char_dict = character_counter(file_contents)
    dict_list = dict_sorter(char_dict)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in dict_list:
        if i["char"].isalpha():
            print(f'{i["char"]}: {i["num"]}')
        else:
            continue
main()