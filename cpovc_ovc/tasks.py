from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from utilities.auto_update_ovc_viralload import UpdateViralLoad

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='5', hour='0', day_of_week='sun')),
    name="update_viralload_every_sunday",
    ignore_result=True
)
def update_viralload_every_sunday():
    # updates ovc viral load every sunday at 00.05
    update_viralload = UpdateViralLoad()
    update_viralload.loop_through_data()
    logger.info("Updated ovc viral load")