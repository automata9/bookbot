def get_num_words(string):
    count = 0
    list_of_words = string.split()
    
    for word in list_of_words:
        count += 1
    
    return count

def character_counter(string):
    count_dict = {}
    string = string.lower()

    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    
    return count_dict