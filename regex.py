import re


def word_search(sentence, search_word):
    """
    Function to find given word in sentence or not
    Parameter: sentence(string), search_word(string)
    return: True / false (boolean)
    """
    return True if re.search(search_word, sentence) else False

def word_search_with_endspan(sentence, search_word, endspan=None):
    """
    Function to find given word in sentence or not
    Parameter: sentence(string), search_word(string)
    return: search word with given span / only return word
    """ 
    if endspan:
        return re.search(search_word+"\w"*endspan, sentence)
    else:
        return re.search(search_word, sentence)

def remove_duplicates_letter(word):
    """
    Function to remove duplicates
    Parameter: word (string)
    return: string
    """
    return re.sub(r"(.)(?=\1+)", "", word)

def separate_numbers_alphabets(str):
    """
    Function to separate the numbers and alphabets
    Parameter: string
    return : numbers and alphabets (string)
    """
    numbers = re.findall(r'[0-9]+', str)
    alphabets = re.findall(r'[a-zA-Z]+', str)
    return *numbers, *alphabets 

def count_word_occurance(sentence, str):
    """
    Function to count occurance of the given word in the sentence
    Parameter : sentence, word
    return: count (number)
    """
    return len(re.findall(str, sentence))

def count_repeated_char(str):
    """
    Function to count repeated character of the given word.
    Paramerter: String
    return: dict
    """
    repeated_chars = re.findall(r'([a-zA-Z])+', str)
    count_dict = {}
    for char in repeated_chars:
        count_dict[char] = str.count(char)

    # Filter to include only repeated characters
    repeated_count = {char: count for char, count in count_dict.items()}
    return repeated_count