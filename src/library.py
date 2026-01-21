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

