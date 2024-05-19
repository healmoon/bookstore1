class BookService:
    def __init__(self, storage):
        self.storage = storage

    def add(self, book):
        return self.storage.add(book)

    def delete(self, id):
        self.storage.delete(id)

    def get_all(self):
        return self.storage.get_all()

    def get_book_by_id(self, id):
        return self.storage.get_book_by_id(id)
