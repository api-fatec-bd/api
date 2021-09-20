from apscheduler.schedulers.background import BackgroundScheduler

from .filtrosETL import countMessages,countUsers, countSessions, countRooms, totalMessagesRoom

PERIODO_HORAS = 24

def startCountMessages():
    scheduler = BackgroundScheduler()
    scheduler.add_job(countMessages, 'interval', hours=PERIODO_HORAS)
    scheduler.start()

def startCountSessions():
    scheduler = BackgroundScheduler()
    scheduler.add_job(countSessions, 'interval', hours=PERIODO_HORAS)
    scheduler.start()

def startCountRooms():
    scheduler = BackgroundScheduler()
    scheduler.add_job(countRooms, 'interval', hours=PERIODO_HORAS)
    scheduler.start()

def startTotalMessagesRoom():
    scheduler = BackgroundScheduler()
    scheduler.add_job(totalMessagesRoom, 'interval', hours=PERIODO_HORAS)
    scheduler.start()


def startCountUsers():
    scheduler = BackgroundScheduler()
    scheduler.add_job(countUsers, 'interval', hours=PERIODO_HORAS)
    scheduler.start()



