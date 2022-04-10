import os
import django
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

scheduler = BlockingScheduler()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news.settings")
django.setup()


@scheduler.scheduled_job(IntervalTrigger(seconds=3))
def update_posts_votes():
    from post import models
    print("here")
    models.Post.objects.all().update(votes_number=0)


scheduler.start()
