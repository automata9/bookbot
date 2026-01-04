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

def get_num(dict):
    return dict["num"]


def dict_sorter(dict):
    dict_list = []
    
    for key in dict:
        dict_list.append({"char": key, "num": dict[key]})
    
    dict_list.sort(key=get_num, reverse=True)
    return dict_list
    