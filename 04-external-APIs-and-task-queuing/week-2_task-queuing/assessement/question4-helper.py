# Question 4 & 5: Add any imports you need
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from books.models import Book


def update_count_for_author(author):
    """Update the count of books (`book_count`) for `author`."""
    author.book_count = Book.objects.filter(author=author).count()
    author.save()


def setup_book_count_update_schedule():
    """Set up an `IntervalSchedule` and `PeriodicTask` to execute `books.tasks.author_count_update` daily."""
    # Question 4: Implement this function body
    day_schedule, _ = IntervalSchedule.objects.get_or_create(
        every=1, period=IntervalSchedule.DAYS
    )
    PeriodicTask.objects.create(
        name="author_count_update",
        task="books.tasks.author_count_update",
        interval=day_schedule,
    )


@shared_task
def author_notify(all_authors):
    # Question 5: Decorate this function
    if all_authors:
        print("Notifying all authors...")
    else:
        print("Notifying some authors...")
