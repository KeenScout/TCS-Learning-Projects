import re


def findallwords(text):
    text_altered = text.lower()
    all_words = re.findall(r"[a-z]+", text_altered)
    return all_words
