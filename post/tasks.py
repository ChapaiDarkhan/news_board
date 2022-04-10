import logging
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

scheduler = BlockingScheduler()

logger = logging.getLogger(__name__)


@scheduler.scheduled_job(IntervalTrigger(seconds=3))
def train_model():
    logger.info('Book %s is exported', datetime.now())
    print('dask train_model! The time is: %s' % datetime.now())


scheduler.start()
