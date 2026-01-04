def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def num_of_words(string):
    count = 0
    list_of_words = string.split()
    
    for word in list_of_words:
        count += 1
    
    return count
def main(): 
    file_contents = get_book_text('./books/frankenstein.txt')
    num_words = num_of_words(file_contents)
    print(f"Found {num_words} total words")

main()