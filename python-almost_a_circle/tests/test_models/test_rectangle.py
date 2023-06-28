import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys

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

    def test_rectangle_initialization(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertIsNone(rect.id)

    def test_rectangle_width_validation(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("invalid", 10)
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

    def test_rectangle_height_validation(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, "invalid")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            rect = Rectangle(5, -10)

    def test_rectangle_x_validation(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, "invalid")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, -1)

    def test_rectangle_y_validation(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, 0, "invalid")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, 0, -1)

    def test_rectangle_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)
        rect.width = 10
        rect.height = 3
        self.assertEqual(rect.area(), 30)

    def test_display(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        r = Rectangle(3, 4, 2, 1)
        r.display()

        sys.stdout = sys.__stdout__

        expected_output = "###\n###\n###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_representation(self):
        r = Rectangle(4, 5, 1, 2, 10)
        expected_output = "[Rectangle] (10) 1/2 - 4/5"
        self.assertEqual(str(r), expected_output)
    
    def test_update(self):
        r = Rectangle(1, 1, 1, 1, 1)

        r.update(2)
        self.assertEqual(r.id, 2)

        r.update(3, 4)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.width, 4)

        r.update(5, 6, 7)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)

        r.update(8, 9, 10, 11)
        self.assertEqual(r.id, 8)
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 11)

        r.update(12, 13, 14, 15, 16)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 13)
        self.assertEqual(r.height, 14)
        self.assertEqual(r.x, 15)
        self.assertEqual(r.y, 16)

        r.update(id=17)
        self.assertEqual(r.id, 17)

        r.update(width=18, height=19)
        self.assertEqual(r.width, 18)
        self.assertEqual(r.height, 19)

        r.update(x=20, y=21)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 21)

    def test_to_dictionary(self):
        obj = Rectangle(10, 20, 1, 100, 200)
        expected_dict = {
            "x": 10,
            "y": 20,
            "id": 1,
            "height": 100,
            "width": 200
        }
        self.assertEqual(obj.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()