
from .conexaoMongoDB import selectBanco

#IMPORT DE TABELAS DO MODELS.PY

from .models import tbCountRooms, tbCountUsers, tbCountMessages, tbMessagesRoom, tbCountSessions


#CRIAÇÃO DE FILTTROS PARA IMPLEMENTAR O BANCO QUE SERÁ ENVIADO AO DW

################################################ rocketchat.rocketchat_message #####################################################################

#TOTAL DE MENSAGENS
def countMessages():
    messages = selectBanco().rocketchat_message
    count_messages = messages.count_documents({})

    # CADASTRAR DADO NA TABELA tbCountMessages
    tb_count_messages = tbCountMessages()
    tb_count_messages.id = 1
    tb_count_messages.totalMessages = count_messages
    tb_count_messages.save()

    return count_messages


################################################ rocketchat.rocketchat_sessions #####################################################################

#TOTAL DE SESSÕES
def countSessions():
    sessions = selectBanco().rocketchat_sessions
    count_sessions = sessions.count_documents({})

    # CADASTRAR DADO NA TABELA tbCountSessions
    tb_count_sessions = tbCountSessions()
    tb_count_sessions.id = 1
    tb_count_sessions.totalSessions = count_sessions
    tb_count_sessions.save()
    return count_sessions


################################################ rocketchat.rocketchat_room #####################################################################

#TOTAL DE ROOM'S
def countRooms():
    rooms = selectBanco().rocketchat_room
    count_rooms = rooms.count_documents({})

    # CADASTRAR DADO NA TABELA tbCountRooms
    tb_count_rooms = tbCountRooms()
    tb_count_rooms.id = 1
    tb_count_rooms.totalRooms = count_rooms
    tb_count_rooms.save()

    return count_rooms

#TOTAL DE MENSAGENS POR SALA
def totalMessagesRoom():
    rooms = selectBanco().rocketchat_room
    messages_room = rooms.find()

    # EXCLUIR DADOS DA TABELA PARA INSERIR NOVOS
    tbMessagesRoom.objects.all().delete()

    # CADASTRAR DADO NA TABELA tbMessagesRoom
    tb_messages_room = tbMessagesRoom()
    count = 0
    for message in messages_room:
        count = count + 1
        tb_messages_room.id = count
        tb_messages_room.roomName = message['name']
        tb_messages_room.totalMessages = message['msgs']
        tb_messages_room.save()

    return vetor_messagesRoom


################################################ rocketchat.users #####################################################################

#TOTAL DE USUÁRIOS
def countUsers():
    users = selectBanco().users
    count_users = users.find()

    count = 0
    for user in count_users:
        if user['type'] == "user":
            count = count + 1

    # CADASTRAR DADO NA TABELA tbCountUsers
    tb_count_user = tbCountUsers()
    tb_count_user.id = 1
    tb_count_user.totalUsers = count_users

    return count

