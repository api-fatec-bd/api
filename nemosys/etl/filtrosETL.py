
from .conexaoMongoDB import selectBanco


#CRIAÇÃO DE FILTTROS PARA IMPLEMENTAR O BANCO QUE SERÁ ENVIADO AO DW

################################################ rocketchat.rocketchat_message #####################################################################

#TOTAL DE MENSAGENS
def countMessages():
    messages = selectBanco().rocketchat_message
    count_messages = messages.count_documents({})
    return count_messages


################################################ rocketchat.rocketchat_sessions #####################################################################

#TOTAL DE SESSÕES
def countSessions():
    sessions = selectBanco().rocketchat_sessions
    count_sessions = sessions.count_documents({})
    return count_sessions


################################################ rocketchat.rocketchat_room #####################################################################

#TOTAL DE ROOM'S
def countRooms():
    rooms = selectBanco().rocketchat_room
    count_rooms = rooms.count_documents({})
    return count_rooms

#TOTAL DE MENSAGENS POR SALA
def totalMessagesRoom():
    rooms = selectBanco().rocketchat_room
    messages_room = rooms.find()
    vetor_messagesRoom = []
    for message in messages_room:
        linha_vetor = [message['name'], message['msgs']]
        vetor_messagesRoom.append(linha_vetor)
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
    return count
