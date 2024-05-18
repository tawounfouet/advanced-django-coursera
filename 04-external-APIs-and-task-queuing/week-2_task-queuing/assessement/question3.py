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