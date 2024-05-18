# helpers.py

# Question 4 & 5: Add any imports you need
from django_celery_beat.models import IntervalSchedule, PeriodicTask, CrontabSchedule

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



def setup_author_notify_schedule():
    """
    Set up a `CrontabSchedule` and `PeriodicTask` to execute `books.tasks.author_notify` at 6AM on the first day of
    every month.
    """
    # Question 5: Implement this function body
    crontab_schedule = CrontabSchedule.objects.create(day_of_month=1, hour=6, minute=0)
    PeriodicTask.objects.create(
        name="author_notify",
        task="books.tasks.author_notify",
        crontab=crontab_schedule,
        args="[true]",
    )