import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_str(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

        s = Square(10, 0, 0, 4)
        self.assertEqual(str(s), "[Square] (4) 0/0 - 10")

        s = Square(3, 2, 2)
        self.assertEqual(str(s), "[Square] (None) 2/2 - 3")

if __name__ == '__main__':
    unittest.main()
