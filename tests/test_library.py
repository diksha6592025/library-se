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
# ---------- Sprint 2 Tests ----------
    def test_borrow_book(self):
        lib = Library()
        lib.add_book("B2", "AI", "OpenAI")
        lib.borrow_book("B2")
        self.assertTrue(lib.books["B2"]["borrowed"])

    def test_borrow_unavailable_book(self):
        lib = Library()
        lib.add_book("B3", "ML", "Andrew")
        lib.borrow_book("B3")
        with self.assertRaises(ValueError):
            lib.borrow_book("B3")

    def test_return_book(self):
        lib = Library()
        lib.add_book("B4", "DS", "Someone")
        lib.borrow_book("B4")
        lib.return_book("B4")
        self.assertFalse(lib.books["B4"]["borrowed"])

if __name__ == "__main__":
    unittest.main()
