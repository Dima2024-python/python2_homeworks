class LibraryItem:
    def __init__(self, title: str, author_or_director: str, year: int):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}"


library = LibraryItem("iii", "kkk", 90)
print(library)
