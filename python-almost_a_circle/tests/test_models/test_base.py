import unittest
from models.base import Base
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
import os

class TestBase(unittest.TestCase):

    def test_base_id_generation(self):
        base1 = Base()
        base2 = Base()
        base3 = Base(89)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 89)

    def test_base_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_base_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_base_to_json_string_with_data(self):
        json_string = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_string, '[{"id": 12}]')

    def test_base_to_json_string_with_data_returning_string(self):
        json_string = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(json_string, str)

    def test_base_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_base_from_json_string_empty_list(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_base_from_json_string_with_data(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{'id': 89}])

    def test_base_from_json_string_with_data_returning_list(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)
  
    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)
            
    def test_create_rectangle(self):
        dictionary = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        rect = Rectangle.create(**dictionary)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_create_square(self):
        dictionary = {'id': 2, 'size': 7, 'x': 4, 'y': 5}
        square = Square.create(**dictionary)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def setUp(self):
        self.file_name = "Base.json"
        json_data = '[{"id": 1, "width": 10, "height": 5, "x": 0, "y": 0}, {"id": 2, "size": 7, "x": 2, "y": 3}]'
        with open(self.file_name, "w") as file:
            file.write(json_data)

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_load_from_file_file_not_found(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 0)

if __name__ == '__main__':
    unittest.main()
