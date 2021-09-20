from django.db import models

# Create your models here.

class tbCountMessages(models.Model):
    id = models.IntegerField("ID", primary_key=True)
    totalMessages = models.IntegerField("Total de mensagens", null=False)

class tbCountSessions(models.Model):
    id = models.IntegerField("ID", primary_key=True)
    totalSessions = models.IntegerField("Total de sessões", null=False)

class tbCountRooms(models.Model):
    id = models.IntegerField("ID", primary_key=True)
    totalRooms = models.IntegerField("Total de salas", null=False)

class tbMessagesRoom(models.Model):
    id = models.IntegerField("ID", primary_key=True)
    roomName = models.CharField("Nome da sala", null=False, max_length=50)
    totalMessages = models.IntegerField("Total", null=False)

class tbCountUsers(models.Model):
    id = models.IntegerField("ID", primary_key=True)
    totalUsers = models.IntegerField("Total de usuários", null=False)



