def get_num_words(text):
    return len(text.split())

def sort_by(sorted_dict):
    return sorted_dict[1]

def get_letter_frequency(text):
    lowercase = text.lower()
    result = {}
    for char in lowercase:
        if char.isalpha() == True:
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1
    return sorted(result.items(), key = sort_by, reverse = True)