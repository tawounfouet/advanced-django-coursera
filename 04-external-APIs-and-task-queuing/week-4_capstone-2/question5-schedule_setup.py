#def schedule_setup():
#    pass

from django_celery_beat.models import IntervalSchedule, PeriodicTask


def schedule_setup():
    interval_schedule = IntervalSchedule.objects.create(
        every=1, period=IntervalSchedule.MINUTES
    )

    PeriodicTask.objects.create(
        task="movies.tasks.notify_of_starting_soon", interval=interval_schedule
    )