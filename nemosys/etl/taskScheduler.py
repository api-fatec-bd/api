from apscheduler.schedulers.background import BackgroundScheduler
from .ETL import usersETL, classesETL, coursesETL, subjectsETL, sessionsETL, lessonsETL

# hours
schedule = 24


def ETLschedule():
    scheduler = BackgroundScheduler()
    scheduler.add_job(usersETL, 'interval', hours=schedule)
    scheduler.add_job(sessionsETL, 'interval', hours=schedule)
    scheduler.add_job(coursesETL, 'interval', hours=schedule)
    scheduler.add_job(subjectsETL, 'interval', hours=schedule)
    scheduler.add_job(classesETL, 'interval', hours=schedule)
    scheduler.add_job(lessonsETL, 'interval', hours=schedule)
    scheduler.start()



