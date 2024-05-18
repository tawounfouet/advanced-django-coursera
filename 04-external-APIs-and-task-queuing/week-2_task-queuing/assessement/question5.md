# Task Queuing: Question 5

## Question 5
The author_notify() function in books/tasks.py is a function that (pretends to) notify authors every month. It can be called with the argument True to “notify” all the users or False to “notify” just some. You must make adjustments to this file.

We want all the authors to be notified at 6AM on the first day of the month. The function setup_author_notify_schedule() in books/helpers.py need to be turned into a Celery task and then implemented to setup the schedule. Use a CrontabSchedule, you will need to set the day_of_month, hour and minute fields. The PeriodicTask must have JSON encoded args set: a list with one element, True. It should also have a name but it does not matter what this is, as long as it is different from the name used in Question 4.

You can execute the setup_author_notify_schedule() to test it, by using the question5 management command:
python3 manage.py question5

As with Question 4, you might need to wait a while to test this with Celery beat, so instead you can check through the Django admin that it looks OK, or run the unit tests for this question.
TRY IT

Note: use the same login information for the Django admin as was used in Question 4.
START DEV SERVER

View Admin Page

## Task
```python
# helpers.py

# Question 4 & 5: Add any imports you need

from books.models import Book


def update_count_for_author(author):
    """Update the count of books (`book_count`) for `author`."""
    author.book_count = Book.objects.filter(author=author).count()
    author.save()


def setup_book_count_update_schedule():
    """Set up an `IntervalSchedule` and `PeriodicTask` to execute `books.tasks.author_count_update` daily."""
    # Question 4: Implement this function body


def setup_author_notify_schedule():
    """
    Set up a `CrontabSchedule` and `PeriodicTask` to execute `books.tasks.author_notify` at 6AM on the first day of
    every month.
    """
    # Question 5: Implement this function body
```

```python
# Task.py

# Question 2: Add any imports you need here


def author_count_update():
    """Call `update_count_for_author()` for every `Author`."""
    print("Updating author counts for all authors")
    # Question 2: Implement and decorate this function


def author_notify(all_authors):
    # Question 5: Decorate this function
    if all_authors:
        print("Notifying all authors...")
    else:
        print("Notifying some authors...")
```


## Solution
```python
# Helpers.py

from django_celery_beat.models import IntervalSchedule, PeriodicTask, CrontabSchedule

# existing update_count_for_author and setup_book_count_update_schedule functions

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
```

- Add CrontabSchedule to the list of imports from django_celery_beat.models.
- Create a crontab schedule where day_of_month is 1, hour is 6, and minute is 0.
- Create a periodic task where the name is different from that in Question 4.
- The periodic task should invoke author_notify and make use of the crontab schedule.
- Be sure to pass true (as a list) to args so that all authors are notified.

```python
# Task.py

@shared_task
def author_notify(all_authors):
    # Question 5: Decorate this function
    if all_authors:
        print("Notifying all authors...")
    else:
        print("Notifying some authors...")
```

- Decorate the author_notify function with @shared_task.