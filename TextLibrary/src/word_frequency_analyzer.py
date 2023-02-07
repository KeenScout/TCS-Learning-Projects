from collections import Counter
from TextLibrary.src.utils.text_utils import findallwords


# TODO wrap in class
def calculate_highest_frequency(text):
    # TODO check if input is clean

    # run the code to find the highest frequency word

    all_words = findallwords(text)
    count = Counter(sorted(all_words))
    most_common = count.most_common(1)
    return most_common


def calculate_frequency_for_word(text, word):
    # TODO check if input is clean
    # run the code for find the frequency of a word
    all_words = findallwords(text)
    count = all_words.count(word)
    return count


def calculate_most_frequent_n_words(text, n):
    # TODO check if input is clean

    # run the code to find the n most frequent words
    all_words = findallwords(text)
    count = Counter(sorted(all_words))
    n_frequently_encountered = count.most_common(n)
    return n_frequently_encountered
