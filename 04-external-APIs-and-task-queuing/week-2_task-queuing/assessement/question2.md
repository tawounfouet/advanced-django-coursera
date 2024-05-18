# Task Queuing: Question 2

## Question 2
The function update_count_for_author() in books/helpers.py counts the number of Books by the passed in Author, then updates book_count on that Author and saves it. We want a Celery task to perform this for every author in the database. The function author_count_update() in books/tasks.py has been started but must be finished:

- Update author_count_update() so that it can be used as Celery task.
- Implement the rest of the function body to call update_count_for_author() for every author. This should only be a couple of lines of code.

A management command has been added to help you, by triggering the author_count_update() task through celery. It’s called question2, and can be executed like so:

python3 manage.py question2

You will need to have a Celery worker running to execute the task. It can be started like this:
celery -A module2 worker -l INFO

## Task
```python
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
from books.helpers import update_count_for_author
from books.models import Author
from celery import shared_task

@shared_task
def author_count_update():
    """Call `update_count_for_author()` for every `Author`."""
    print("Updating author counts for all authors")
    # Question 2: Implement and decorate this function
    for author in Author.objects.all():
        update_count_for_author(author)
```

- Import the update_count_for_author function, the Author model, and the shared_task decorator.
- Decorate the author_count_update function with @shared_task.
- Iterate over all the Author objects.
- Pass each Author object to the update_count_for_author function.