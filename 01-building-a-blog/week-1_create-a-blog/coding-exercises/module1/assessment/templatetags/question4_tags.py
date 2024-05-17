from django import template
from django.template.loader import render_to_string
from assessment.models import Comment  # Import Comment from the correct location

register = template.Library()

@register.simple_tag
def comments_for_thing(thing):
    # Fetch comments related to the given Thing and sort them alphabetically by content
    comments = Comment.objects.filter(thing=thing).order_by('content')
    # Render the comments using the comments.html template
    return render_to_string('comments.html', {'comments': comments})
