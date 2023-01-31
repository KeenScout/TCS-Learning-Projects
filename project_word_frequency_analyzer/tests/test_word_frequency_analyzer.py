from project_word_frequency_analyzer.src import word_frequency_analyzer


def test_calculate_highest_frequency():
    # most basic functionality tests
    assert word_frequency_analyzer.calculate_highest_frequency("The sun shines over the lake") == [('the', 2)]
    assert word_frequency_analyzer.calculate_highest_frequency("tHe SuN SHInes over ThE lake") == [('the', 2)]


def test_calculate_frequency_for_word():
    # most basic functionality tests
    assert word_frequency_analyzer.calculate_frequency_for_word("The sun shines over the lake", "the") == 2
    assert word_frequency_analyzer.calculate_frequency_for_word("tHe SuN SHInes over ThE lake", "the") == 2


def test_calculate_most_frequent_n_words():
    # most basic functionality tests
    assert word_frequency_analyzer.calculate_most_frequent_n_words("the sun shines over the lake", 3) == \
           [('the', 2), ('lake', 1), ('over', 1)]
    assert word_frequency_analyzer.calculate_most_frequent_n_words("tHe SuN SHInes over ThE lake", 3) == \
           [('the', 2), ('lake', 1), ('over', 1)]
    