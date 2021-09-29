from django.db import models

# Create your models here.


class dim_usuario(models.Model):
    id_usuario = models.TextField("id user", primary_key=True)
    nome_usuario = models.TextField("nome_usuario", null=False)
    email = models.TextField("email", null=False)
    codigo_permissao = models.IntegerField("codigo_permissao", null=False)
    descricao_permissao = models.TextField("descricao_permissao", null=False)
    tel_1 = models.TextField("tel_1", null=True)
    tel_2 = models.TextField("tel_2", null=True)

'''
CREATE TABLE dim_usuario (
  id_usuario BIGINT IDENTITY NOT NULL PRIMARY KEY NONCLUSTERED,
  nome_usuario VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  codigo_permissao INT NOT NULL,
  descricao_permissao VARCHAR(50) NOT NULL,
  tel_1 VARCHAR(45) NULL,
  tel_2 VARCHAR(45) NULL
 );
'''



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



