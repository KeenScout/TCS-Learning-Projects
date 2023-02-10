from collections import Counter
from utils.text_utils import findallwords


class WordFrequencyAnalyzer:

    def calculate_highest_frequency(text):
        # checking if input is clean
        if not isinstance(text, str):
            raise TypeError("text should be a string")
        if len(text.strip()) == 0:
            raise ValueError("text is empty")
        # run the code to find the highest frequency word
        all_words = findallwords(text)
        count = Counter(sorted(all_words))
        most_common = count.most_common(1)
        return most_common

    def calculate_frequency_for_word(text, word):
        # checking if text is clean
        if not isinstance(text, str):
            raise TypeError("text should be a string")
        if len(text.strip()) == 0:
            raise ValueError("text is empty")
        # checking if word is clean
        if not isinstance(word, str):
            raise TypeError("word should be a string")
        if len(word.strip()) == 0:
            raise ValueError("word is empty")

        # run the code for find the frequency of a word
        all_words = findallwords(text)
        count = all_words.count(word)
        return count

    def calculate_most_frequent_n_words(text, n):
        # checking if text is clean
        if not isinstance(text, str):
            raise TypeError("text should be a string")
        if len(text.strip()) == 0:
            raise ValueError("text is empty")
        # checking if n is clean
        if not isinstance(n, int):
            raise TypeError("N should be a int")
        if n < 1:
            raise ValueError("N should be a positive int")

        # run the code to find the n most frequent words
        all_words = findallwords(text)
        count = Counter(sorted(all_words))
        n_frequently_encountered = count.most_common(n)
        return n_frequently_encountered
