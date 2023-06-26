import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def test_multiple(self):

        r1 = Rectangle()
        r2 = Rectangle()
        self.assertEqual(r1.id, r2.id - 1)

        r3 = Rectangle()
        self.assertEqual(r1.id, r2.id, r3.id - 2)

        r1 = Rectangle(None)
        r2 = Rectangle(None)
        self.assertEqual(r1.id, r2.id - 1)

        self.assertEqual(20, Rectangle().id)


if __name__ == '__main__':
    unittest.main()