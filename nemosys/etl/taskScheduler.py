from apscheduler.schedulers.background import BackgroundScheduler
from .ETL import usersETL

# hours
schedule = 24


def usersETLschedule():
    scheduler = BackgroundScheduler()
    scheduler.add_job(usersETL, 'interval', hours=schedule)
    scheduler.start()


