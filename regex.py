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
    retunr: count (number)
    """
    return len(re.findall(str, sentence))
