from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from utilities.auto_update_facility_list import KMHFLFacilities

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='5', hour='0', day_of_week='mon')),
    name="update_facilities_every_monday",
    ignore_result=True
)
def update_facilities_every_monday():
    # updates latest facilities every monday at 00.05
    facilities = KMHFLFacilities()
    facilities.get_newest_facilities()
    logger.info("Updated master facility list")