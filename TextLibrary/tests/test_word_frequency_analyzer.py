import pytest

from word_frequency_analyzer import WordFrequencyAnalyzer
from tests.test_data.inputs import *


# Tests to validate that the Highest Frequency function works
@pytest.mark.parametrize("test_input, expected", TEST_DATA_HIGHEST)
def test_calculate_highest_frequency(test_input, expected):
    assert WordFrequencyAnalyzer.calculate_highest_frequency(test_input) == expected


@pytest.mark.parametrize("test_input, error_msg", TEST_DATA_HIGHEST_NOT_STRING)
def test_calculate_highest_frequency_type_error(test_input, error_msg):
    with pytest.raises(TypeError) as exc_info:
        WordFrequencyAnalyzer.calculate_highest_frequency(test_input)
    assert str(exc_info.value) == error_msg


@pytest.mark.parametrize("test_input, error_msg", TEST_DATA_HIGHEST_EMPTY)
def test_calculate_highest_frequency_value_error(test_input, error_msg):
    with pytest.raises(ValueError) as exc_info:
        WordFrequencyAnalyzer.calculate_highest_frequency(test_input)
    assert str(exc_info.value) == error_msg


# Tests to validated that the Frequency For Word function works
@pytest.mark.parametrize("test_input, word, expected", TEST_DATA_WORD)
def test_calculate_frequency_for_word(test_input, word, expected):
    assert WordFrequencyAnalyzer.calculate_frequency_for_word(test_input, word) == expected


@pytest.mark.parametrize("test_input, word, error_msg", TEST_DATA_WORD_NOT_STRING)
def test_calculate_frequency_for_word_type_error(test_input, word, error_msg):
    with pytest.raises(TypeError) as exc_info:
        WordFrequencyAnalyzer.calculate_frequency_for_word(test_input, word)
    assert str(exc_info.value) == error_msg


@pytest.mark.parametrize("test_input, word, error_msg", TEST_DATA_WORD_EMPTY)
def test_calculate_frequency_for_word_value_error(test_input, word, error_msg):
    with pytest.raises(ValueError) as exc_info:
        WordFrequencyAnalyzer.calculate_frequency_for_word(test_input, word)
    assert str(exc_info.value) == error_msg


# Tests to validated that the Most Frequent N Words function works
@pytest.mark.parametrize("test_input, number, expected", TEST_DATA_FREQUENT)
def test_calculate_most_frequent_n_words(test_input, number, expected):
    assert WordFrequencyAnalyzer.calculate_most_frequent_n_words(test_input, number) == expected


@pytest.mark.parametrize("test_input, number, error_msg", TEST_DATA_FREQUENT_TYPE)
def test_calculate_most_frequent_n_words_type_error(test_input, number, error_msg):
    with pytest.raises(TypeError) as exc_info:
        WordFrequencyAnalyzer.calculate_most_frequent_n_words(test_input, number)
    assert str(exc_info.value) == error_msg


@pytest.mark.parametrize("test_input, number, error_msg", TEST_DATA_FREQUENT_EMPTY)
def test_calculate_most_frequent_n_words_value_error(test_input, number, error_msg):
    with pytest.raises(ValueError) as exc_info:
        WordFrequencyAnalyzer.calculate_most_frequent_n_words(test_input, number)
    assert str(exc_info.value) == error_msg
