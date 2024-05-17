from collections import namedtuple

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render

from assessment.models import Thing, Comment


def question2(request):
    # This View does not need to be changed for Question 2
    return render(request, "question2.html")


def question3(request):
    # This View does not need to be changed for Question 3
    User = namedtuple("User", ["first_name", "last_name"])
    user1 = User("Leo", "Lucio")
    user2 = User("Lily", None)
    user3 = User('<a href="bad-site">Evil</a>', "Hacker > You")

    return render(
        request, "question3.html", {"user1": user1, "user2": user2, "user3": user3}
    )


def question4(request):
    # This View does not need to be changed for Question 4
    u, created = get_user_model().objects.get_or_create(username="test_user")
    thing, created = Thing.objects.get_or_create(name="My Cardigan", owner=u)
    thing_ct = ContentType.objects.get_for_model(Thing)
    Comment.objects.get_or_create(
        content="A cardigan is the best type of clothing.",
        object_id=thing.id,
        content_type=thing_ct,
    )
    Comment.objects.get_or_create(
        content="I agree, it's great.", object_id=thing.id, content_type=thing_ct
    )
    Comment.objects.get_or_create(
        content="Not sure about these statements.",
        object_id=thing.id,
        content_type=thing_ct,
    )
    return render(request, "question4.html", {"thing": thing})
