from collections import Counter
import string


class WordFrequency:
    #getting blok of text form the user
    text = input("Please provide a text:\n")

    #getting the word that they would like to know the frequency of from the user
    while True:
        word = str(input("Please provide a word for which you want to know the frequency:\n"))
        if word.lower() not in text.lower():
            print("Please enter a word that is in the text. \n")
            continue
        break

    #getting a postive integer from the user
    while True:
        try:
            frequency = int(input("please provide the desired lenght of the list you want:\n"))
            if frequency <0:
                print("please enter a postive integer\n.")
                continue 
            break
        except ValueError:
            print("please enter a integer.\n")
            continue


class WordFrequencyAnalyzer:
    # Return the highest frequency found in the text
    def calculate_highest_frequency(self, text):
        text = text.split()
        count = Counter(sorted(text))
        mostCommon = count.most_common(1)
        return mostCommon  

    #return the frequency of a specified word
    def calculate_frequency_for_word(self, text, word):
        count = text.lower().split().count(word)
        return count

    #return a list of the most frequent N words
    def calculate_most_frequent_n_words(text, n):
        text = text.split()
        count = Counter(sorted(text))
        NFrequentlyencountered = count.most_common(n)
        return NFrequentlyencountered           


if __name__ == '__main__':
    usertext = WordFrequency.text
    text = "".join([word for word in usertext if word in string.ascii_letters + ' ']).lower()
    userword = WordFrequency.word
    n = WordFrequency.frequency


    #printing the highest frequency word
    print("\nThe most common word in the text is: {}\n".format(WordFrequencyAnalyzer().calculate_highest_frequency(text)))
    #printing how many times a word was found
    print("the word {} was found {} times\n".format(userword, WordFrequencyAnalyzer().calculate_frequency_for_word(text, userword)))
    #printing the list 
    print("List of the {} most common words in the text:".format(n))
    print("{}\n".format(WordFrequencyAnalyzer.calculate_most_frequent_n_words(text, n)))
