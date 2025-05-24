import unittest
import sys
import os
import tempfile
import shutil

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utils import load_data_from_file, save_data_to_file


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, 'test_data.txt')

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_load_data_from_file(self):
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("Абаев, Тимур\n")
            f.write("Бобков, Андрей\n")
            f.write("Видерт, Руслан\n")

        data = load_data_from_file(self.test_file)

        self.assertEqual(len(data), 3)
        self.assertEqual(data[0], ("Абаев", "Тимур"))
        self.assertEqual(data[1], ("Бобков", "Андрей"))
        self.assertEqual(data[2], ("Видерт", "Руслан"))

    def test_load_empty_file(self):
        open(self.test_file, 'w').close()
        data = load_data_from_file(self.test_file)
        self.assertEqual(len(data), 0)

    def test_load_nonexistent_file(self):
        data = load_data_from_file("nonexistent_file.txt")
        self.assertEqual(len(data), 0)

    def test_save_data_to_file(self):
        test_data = [
            ("Абаев", "Тимур"),
            ("Бобков", "Андрей"),
            ("Видерт", "Руслан")
        ]

        save_data_to_file(self.test_file, test_data)
        with open(self.test_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 3)
        self.assertEqual(lines[0].strip(), "Абаев, Тимур")
        self.assertEqual(lines[1].strip(), "Бобков, Андрей")
        self.assertEqual(lines[2].strip(), "Видерт, Руслан")


if __name__ == '__main__':
    unittest.main()