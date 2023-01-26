from collections import Counter

if __name__ == '__main__':
    def calculate_highest_frequency(text):
        text = text.split()
        count = Counter(sorted(text))
        mostCommon = count.most_common(1)
        return mostCommon

    # return the frequency of a specified word
    def calculate_frequency_for_word( text, word):
        count = text.lower().split().count(word)
        return count

    # return a list of the most frequent N words
    def calculate_most_frequent_n_words(text, n):
        text = text.split()
        count = Counter(sorted(text))
        NFrequentlyencountered = count.most_common(n)
        return NFrequentlyencountered


    text = "The sun shines over the lake".lower()
    userWord = "the"
    n = 2

    # printing the highest frequency word
    print("\nThe most common word in the text is: {}\n".format(calculate_highest_frequency(text)))
    # printing how many times a word was found
    print("the word {} was found {} times\n".format(userWord,calculate_frequency_for_word(text, userWord)))
    # printing the list
    print("List of the {} most common words in the text:".format(n))
    print("{}\n".format(calculate_most_frequent_n_words(text, n)))
