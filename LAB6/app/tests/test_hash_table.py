import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(size=10)
        self.test_data = [
            ("Абаев", "Тимур"),
            ("Бобков", "Андрей"),
            ("Видерт", "Руслан")
        ]

        for key, value in self.test_data:
            self.ht.insert(key, value)

    def test_hash_function1(self):
        self.assertEqual(self.ht.hash_function1("Абаев"), 0 * 33 + 1)
        self.assertEqual(self.ht.hash_function1("Бобков"), 1 * 33 + 15)
        self.assertEqual(self.ht.hash_function1("Видерт"), 2 * 33 + 9)

    def test_hash_function2(self):
        h2 = self.ht.hash_function2("Абаев")
        self.assertTrue(1 <= h2 < 7)

    def test_insert_and_search(self):
        for key, value in self.test_data:
            result = self.ht.search(key)
            self.assertIsNotNone(result)
            self.assertEqual(result['Pi'], value)

        self.assertIsNone(self.ht.search("Несуществующий"))

    def test_insert_duplicate(self):
        with self.assertRaises(Exception) as context:
            self.ht.insert("Абаев", "Дубликат")
        self.assertTrue("уже существует" in str(context.exception))

    def test_delete(self):
        self.assertTrue(self.ht.delete("Абаев"))
        self.assertIsNone(self.ht.search("Абаев"))

        index = self.ht.get_hash("Абаев")
        self.assertEqual(self.ht.table[index]['D'], 1)

        self.assertFalse(self.ht.delete("Несуществующий"))

    def test_collision_handling(self):
        small_ht = HashTable(size=3)
        small_ht.insert("Абаев", "Тимур")
        index1 = small_ht.get_hash("Абаев")
        small_ht.insert("Бобков", "Андрей")
        index2 = small_ht.get_hash("Бобков")
        self.assertNotEqual(index1, index2)
        self.assertEqual(small_ht.table[index2]['C'], 1)

    def test_table_full(self):
        small_ht = HashTable(size=2)
        small_ht.insert("Ключ1", "Значение1")
        small_ht.insert("Ключ2", "Значение2")

        with self.assertRaises(Exception) as context:
            small_ht.insert("Ключ3", "Значение3")
        self.assertTrue("Не удалось вставить элемент" in str(context.exception))


if __name__ == '__main__':
    unittest.main()