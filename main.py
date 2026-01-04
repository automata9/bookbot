from stats import get_num_words, character_counter, dict_sorter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main(): 
    file_contents = get_book_text('./books/frankenstein.txt')
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")

    char_dict = character_counter(file_contents)
    print(char_dict)

    dict_list = dict_sorter(char_dict)
    print(dict_list)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in dict_list:
        if i["char"].isalpha():
            print(f'{i["char"]}: {i["num"]}')
main()