# Task Queuing: Question 3

## Question 3
We’d like the book_count to be updated every time a Book is created or deleted. The functions book_post_save() and book_post_delete() have been written in books/signals.py to do this. They need the receiver hooks set up so they’re run at the right time. Add receiver decorators to them. Make sure the sender is limited to Book.

## Task
```python
# Question 3: Add any imports you need

from books.helpers import update_count_for_author

# Question 3: Decorate these functions


def book_post_save(sender, instance, created, **kwargs):
    """Call `update_count_for_author()` for the saved `Book`."""
    if created:
        update_count_for_author(instance.author)


def book_post_delete(sender, instance, **kwargs):
    """Call `update_count_for_author()` for the deleted `Book`."""
    update_count_for_author(instance.author)
```


## Solution
```python
# Question 3: Add any imports you need
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from books.helpers import update_count_for_author
from books.models import Book

# Question 3: Decorate these functions


@receiver(post_save, sender=Book, dispatch_uid="book_post_save")
def book_post_save(sender, instance, created, **kwargs):
    """Call `update_count_for_author()` for the saved `Book`."""
    if created:
        update_count_for_author(instance.author)


@receiver(post_delete, sender=Book, dispatch_uid="book_post_delete")
def book_post_delete(sender, instance, **kwargs):
    """Call `update_count_for_author()` for the deleted `Book`."""
    update_count_for_author(instance.author)
```

- Import the post_save and post_delete signals.
- Import the receiver decorator.
- Import Book from books.models.
- Decorate the book_post_save function with @receiver.
    - Connect the receiver to the post_save signal.
    - Limit the sender to Book.
    - Give it a unique ID of "book_post_save".
- Decorate the book_post_delete function with @receiver.
    - Connect the receiver to the post_delete signal.
    - Limit the sender to Book.
    - Give it a unique ID of "book_post_delete".