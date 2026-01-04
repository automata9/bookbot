def get_num_words(string):
    count = 0
    list_of_words = string.split()
    
    for word in list_of_words:
        count += 1
    
    return count