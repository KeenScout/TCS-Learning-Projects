import main


def test_calculate_highest_frequency():
    # most basic functionality test
    assert main.calculate_highest_frequency("The sun shines over the lake") == [('the', 2)]


def test_calculate_frequency_for_word():
    # most basic functionality test
    assert main.calculate_frequency_for_word("The sun shines over the lake", "the") == 2


def test_calculate_most_frequent_n_words():
    # most basic functionality test
    assert main.calculate_most_frequent_n_words("the sun shines over the lake", 3) == \
           [('the', 2), ('lake', 1), ('over', 1)]
    assert main.calculate_most_frequent_n_words("tHe SuN SHInes over ThE lake", 3) == \
           [('the', 2), ('lake', 1), ('over', 1)]