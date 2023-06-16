import unittest

max_integer = __import__('6-max_integer').max_integer

class maxTest(unittest.TestCase):
    
    def testEmptyList(self):
        self.assertIsNone(max_integer([]))
        
    def testPositiveNumbers(self):
        numbers = [1, 3, 5, 2, 4]
        result = max_integer(numbers)
        self.assertEqual(result, 5)

    def testNegativeNumbers(self):
        numbers = [-1, -3, -5, -2, -4]
        result = max_integer(numbers)
        self.assertEqual(result, -1)

    def testMixedNumbers(self):
        numbers = [-1, 2, -3, 4, -5]
        result = max_integer(numbers)
        self.assertEqual(result, 4)

    def testDuplicateNumbers(self):
        numbers = [5, 5, 5, 5]
        result = max_integer(numbers)
        self.assertEqual(result, 5)

    def testSingleElement(self):
        numbers = [9]
        result = max_integer(numbers)
        self.assertEqual(result, 9)

    def testLargeList(self):
        numbers = list(range(1000000))
        result = max_integer(numbers)
        self.assertEqual(result, 999999)
    
if __name__ == '__main__':
    unittest.main()
