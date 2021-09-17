from django.apps import AppConfig


class EtlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'etl'

    def ready(self):
        from .taskScheduler import startCountUsers, startCountMessages, startCountSessions, startCountRooms, startTotalMessagesRoom

        startCountMessages()
        startCountUsers()
        startCountSessions()
        startCountRooms()
        startTotalMessagesRoom()