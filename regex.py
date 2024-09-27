import re


def wordsearch(sentence, search_word):
    return True if re.search(search_word, sentence) else False

