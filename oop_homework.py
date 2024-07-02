from pydantic import BaseModel


class LibraryItem(BaseModel):
    def new_book(self, title: str, author_or_director: str, year: int):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year
        pass


    def __str__(self) -> str:
        result = f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}"
        return result





class Magazine:
    def __init__(self, issue_number: int):
        self.issue_number = issue_number


    def info_of_issue_number(self):
        return my_book.__str__() + f', Issue_number: {self.issue_number}'


class DVD:
    def __init__(self, duration: int):
        self.duration = duration


    def info_of_duration(self):
        return my_book.__str__() + f', Duration: {self.duration}'



my_book = LibraryItem(title='hh', author_or_director='tti', year=2007)
print(Book.info_of_pages(pages=55))
