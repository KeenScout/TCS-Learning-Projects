from collections import Counter


def calculate_highest_frequency(text):
    text_altered = text.lower().split()
    count = Counter(sorted(text_altered))
    most_common = count.most_common(1)
    return most_common


# return the frequency of a specified word
def calculate_frequency_for_word(text, word):
    count = text.lower().split().count(word)
    return count


# return a list of the most frequent N words
def calculate_most_frequent_n_words(text, n):
    text = text.lower().split()
    count = Counter(sorted(text))
    n_frequently_encountered = count.most_common(n)
    return n_frequently_encountered


if __name__ == '__main__':
    print("hi")
