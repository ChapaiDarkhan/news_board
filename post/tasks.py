import logging
from post.models import Post
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

scheduler = BlockingScheduler()

logger = logging.getLogger(__name__)


@scheduler.scheduled_job(IntervalTrigger(seconds=3))
def update_posts_votes():
    queryset = Post.objects.all().update(votes_number=0)


scheduler.start()
