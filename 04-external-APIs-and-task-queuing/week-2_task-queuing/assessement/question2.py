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



@shared_task
def author_notify(all_authors):
    # Question 5: Decorate this function
    if all_authors:
        print("Notifying all authors...")
    else:
        print("Notifying some authors...")