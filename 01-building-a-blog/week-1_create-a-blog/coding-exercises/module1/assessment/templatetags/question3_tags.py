from django import template
# Question 3: Add your imports below

register = template.Library()


@register.filter
def full_name(user):
    """
    Question 3: Insert code to build the user's full name below. It should return:
    <em>{{ first_name }}</em>, {{ last_name }}
    if the user has a last name, otherwise:
    {{ first_name }}
    Make sure to escape HTML.
    """
    return ""
