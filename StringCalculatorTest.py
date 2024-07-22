import unittest
from StringCalculator import add
class TestStringCalculator(unittest.TestCase):
        
        def test_expectZeroForEmptyInput(self):
                self.assertEqual(add(""), 0)
                
        def test_expectZeroForSingleZero(self):
                self.assertEqual(add("0"), 0)
                
        def test_expectSumForTwoNumberst(self):
                self.assertEqual(add("1,2"), 3)
                
        def test_ignoreNumbersGreaterThan1000(self):
                self.assertEqual(add("1,2001"), 1)
                
        def test_expectSumWithCustomDelimiter(self):
                self.assertEqual(add("//;\n1;2"), 3)
                
        def test_expectSumWithNewlineDelimiter(self):
                self.assertEqual(add("1\n2,3"),6);

        def test_ignoreNumbersGreaterThan1000(self):
                self.assertEqual(add("1,9001"), 1)

        def test_negative(self):
                self.assertEqual(add("1\n2,3;-3"), 1)




if __name__ == '__main__':
    unittest.main()


