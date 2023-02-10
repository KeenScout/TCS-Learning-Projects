TEST_DATA_HIGHEST = [("The sun shines over the lake", [('the', 2)]),
                     ("ThE SuN ShInEs OvEr tHe LaKE", [('the', 2)]),
                     ("1ThE%SuN2sHiNeS###oVeR^ThE31LaKE###", [('the', 2)])]

TEST_DATA_HIGHEST_NOT_STRING = [(2, "text should be a string")]

TEST_DATA_HIGHEST_EMPTY = [("  ", "text is empty")]

TEST_DATA_WORD = [("The sun shines over the lake", "the", 2),
                  ("ThE SuN ShInEs OvEr tHe LaKE", "the", 2),
                  ("1ThE%SuN2sHiNeS###oVeR^ThE31LaKE###", "the", 2)]

TEST_DATA_WORD_NOT_STRING = [(1, "word", "text should be a string"),
                             ("text", 1, "word should be a string")]

TEST_DATA_WORD_EMPTY = [(" ", "word", "text is empty"),
                        ("text", " ", "word is empty")]

TEST_DATA_FREQUENT = [("The sun shines over the lake", 3, [('the', 2), ('lake', 1), ('over', 1)]),
                      ("ThE SuN ShInEs OvEr tHe LaKE", 3, [('the', 2), ('lake', 1), ('over', 1)]),
                      ("1ThE%SuN2sHiNeS###oVeR^ThE31LaKE###", 3, [('the', 2), ('lake', 1), ('over', 1)])]

TEST_DATA_FREQUENT_TYPE = [(2, 2, "text should be a string"),
                           ("text", "int", "N should be a int")]

TEST_DATA_FREQUENT_EMPTY = [(" ", 1, "text is empty"),
                            ("text", -1, "N should be a positive int")]
