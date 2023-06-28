import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_multiple(self):

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

if __name__ == '__main__':
    unittest.main()
