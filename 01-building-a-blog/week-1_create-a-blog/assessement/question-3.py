from django import template
# Question 3: Add your imports below
from django.utils.html import format_html

register = template.Library()


@register.filter
def full_name(user):
    """
    Question 3: Insert code to build the user's full name below. It should return:
    <em>{{ last_name }}</em>, {{ first_name }}
    if the user has a last name, otherwise:
    {{ first_name }}
    Make sure to escape HTML.
    """
    if user.last_name:
        return format_html("<em>{}</em>, {}", user.first_name, user.last_name)

    return format_html("{}", user.first_name)