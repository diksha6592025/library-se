import unittest
from src.library import Library


class TestLibrary(unittest.TestCase):

    # ---------- Sprint 1 Tests ----------
    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        self.assertIn("B1", lib.books)

    def test_duplicate_book_id(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        with self.assertRaises(ValueError):
            lib.add_book("B1", "Java", "James")

if __name__ == "__main__":
    unittest.main()
