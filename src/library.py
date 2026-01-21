class Library:
    def __init__(self):
        self.books = {}

    # ---------- Sprint 1 ----------
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Book ID already exists")
        self.books[book_id] = {
            "title": title,
            "author": author,
            "borrowed": False
        }
        
# ---------- Sprint 2 ----------
    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")
        if self.books[book_id]["borrowed"]:
            raise ValueError("Book already borrowed")
        self.books[book_id]["borrowed"] = True

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")
        self.books[book_id]["borrowed"] = False
