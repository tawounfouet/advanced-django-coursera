
import logging

from django.http import HttpResponse

# Question 5: Create your logger
logger = logging.getLogger(__name__)


def question5(request):
    # Question 5: Add logger calls here
    logger.debug("A Debug Message")
    logger.warning("A Warning Message")
    logger.critical("A Critical Message")
    return HttpResponse("Hello World")