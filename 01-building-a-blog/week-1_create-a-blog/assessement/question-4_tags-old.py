from django import template

register = template.Library()

# Import the Comment model
from assessment.models import Comment

# Question 4: Register the tag
@register.inclusion_tag('comments.html')
def comments_for_thing(thing):
    # Question 4: Implement code to render the comments for the Thing object below.
    # Sort the comments alphabetically by their content when fetching.
    comments = Comment.objects.filter(content_object=thing).order_by('content')
    return {'comments': comments}
