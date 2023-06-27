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
        
    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

        s.size = 10
        self.assertEqual(s.size, 10)

    def test_size_setter(self):
        s = Square(5)
        s.size = 8
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)

        s.size = 12
        self.assertEqual(s.width, 12)
        self.assertEqual(s.height, 12)

if __name__ == '__main__':
    unittest.main()
