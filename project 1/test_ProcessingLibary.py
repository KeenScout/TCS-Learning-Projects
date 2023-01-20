import unittest
import ProcessingLibary

class TestWordFrequencyAnalyzer(unittest.TestCase):
    
    def test_calculate_highest_frequency(self):
        result = ProcessingLibary.WordFrequencyAnalyzer.calculate_highest_frequency("hello hello how are you")
        self.assertEqual(result, [('hello', 2)])

if __name__ == '__main__':
    unittest.main()