# Requests Module and External APIs: Question 5

## Question 5:
The get_and_save() function in books/mbs_integration.py has been created but its body needs to be completed. It should instantiate a client with get_client_from_settings() and then fetch all the books, saving them to the Django database. Be sure not to double up on Authors

## Task
```python
# Question 5: Add imports you need


def get_and_save():
    """Get all the books from the MyBookStoreClient and store in the local database."""
    # Question 5: Implement this function
```

## Solution
```python
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
```

- Import Author, Book, and get_client_from_settings
- Instantiate a client with get_client_from_settings()
- Iterate over the books
- Use the get_or_create method to avoid duplicates