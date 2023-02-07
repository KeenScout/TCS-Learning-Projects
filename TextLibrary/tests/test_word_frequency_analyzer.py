import pytest

from TextLibrary.src import word_frequency_analyzer
from TextLibrary.tests.test_data.inputs import TEST_DATA_1_HIGHEST, TEST_DATA_1_WORD, TEST_DATA_1_FREQUENT


@pytest.mark.parametrize("test_input, expected", TEST_DATA_1_HIGHEST)
def test_calculate_highest_frequency(test_input, expected):
    # most basic functionality tests
    assert word_frequency_analyzer.calculate_highest_frequency(test_input) == expected


@pytest.mark.parametrize("test_input, word, expected", TEST_DATA_1_WORD)
def test_calculate_frequency_for_word(test_input, word, expected):
    # most basic functionality tests
    assert word_frequency_analyzer.calculate_frequency_for_word(test_input, word) == expected


@pytest.mark.parametrize("test_input, number, expected", TEST_DATA_1_FREQUENT)
def test_calculate_most_frequent_n_words(test_input, number, expected):
    # most basic functionality tests
    assert word_frequency_analyzer.calculate_most_frequent_n_words(test_input, number) == expected
