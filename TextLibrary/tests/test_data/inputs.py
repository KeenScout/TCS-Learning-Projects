TEST_DATA_1_HIGHEST = [("The sun shines over the lake", [('the', 2)]),
                       ("ThE SuN ShInEs OvEr tHe LaKE", [('the', 2)]),
                       ("1ThE%SuN2sHiNeS###oVeR^ThE31LaKE###", [('the', 2)])]

TEST_DATA_1_WORD = [("The sun shines over the lake", "the", 2),
                    ("ThE SuN ShInEs OvEr tHe LaKE", "the", 2),
                    ("1ThE%SuN2sHiNeS###oVeR^ThE31LaKE###", "the", 2)]

TEST_DATA_1_FREQUENT = [("The sun shines over the lake", 3, [('the', 2), ('lake', 1), ('over', 1)]),
                        ("ThE SuN ShInEs OvEr tHe LaKE", 3, [('the', 2), ('lake', 1), ('over', 1)]),
                        ("1ThE%SuN2sHiNeS###oVeR^ThE31LaKE###", 3, [('the', 2), ('lake', 1), ('over', 1)])]
