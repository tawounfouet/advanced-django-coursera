# Question 5: Add imports you need

from books.models import Author, Book
from my_book_store.django_client import get_client_from_settings


def get_and_save():
    """Get all the books from the MyBookStoreClient and store in the local database."""
    # Question 5: Implement this function
    client = get_client_from_settings()
    for book in client.get_books():
        author, _ = Author.objects.get_or_create(name=book.author.name)
        book, _ = Book.objects.get_or_create(
            isbn=book.isbn, defaults={"author": author, "title": book.title}
        )