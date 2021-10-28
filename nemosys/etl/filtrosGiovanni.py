from mongoConnection import mongoConnection



# CRIAR FILTRO PARA ALIMENTAR TABELA DIM_DISCIPLINA

"""""""""
Campos: ID_DISCIPLINA; ID_CURSO; ID_TURMA; DESCRICAO;
"""""""""

def filtroDimDisciplina():
    
    collection_disciplina = mongoConnection()['Logs']['Disciplina'].find()

    return collection_disciplina




# CRIAR FILTRO PARA ALIMENTAR TABELA DIM_CURSO

"""""""""
Campos: ID_CURSO; DESCRICAO; GRADUACAO; DURACAO;
"""""""""

def filtroDimCurso():

    collection_curso = mongoConnection()['Logs']['Curso'].find()

    return collection_curso



# CRIAR FILTRO PARA ALIMENTAR TABELA DIM_AULA

"""""""""
Campos: ID_AULA; DATA_INICIO; DATA_FIM; ID_DISCIPLINA; TITULO; ASSUNTO; DURACAO;
"""""""""

def filtroDimAula():

    collection_aula = mongoConnection()['Logs']['Aula'].find()

    return collection_aula


# CRIAR FILTRO PARA ALIMENTAR TABELA DIM_USUARIO

"""""""""
Campos: ID_USUARIO; NOME_USUARIO; CODIGO_PERFIL; DESCRICAO_PERFIL;
"""""""""

def filtroDimUsuario():

    collection_usuario = mongoConnection()['Logs']['Usuario'].find()

    return collection_usuario


# CRIAR FILTRO PARA ALIMENTAR TABELA FACT_CHAT

"""""""""
Campos: ID_CHAT; DATA_INICIO; DATA_FIM; QUANTIDADE_USUARIO; DESCRICAO; DURACAO;
"""""""""

def filtroFactChat():

    collection_room = mongoConnection()['rocketchat']['rocketchat_room'].find()
    vetor_chat = []
    for room in collection_room:
        id_chat = room['_id']
        data_inicio = room['ts']
        data_fim = room['lm']
        quantidade_usuario = room['usersCount']
        descricao_chat = room['name']
        duracao_horas = (data_fim - data_inicio).total_seconds() / 60
        linha_vetor = [id_chat, data_inicio, data_fim, quantidade_usuario, descricao_chat, duracao_horas]
        vetor_chat.append(linha_vetor)

    return vetor_chat


# CRIAR FILTRO PARA ALIMENTAR TABELA FACT_USUARIO_CHAT

"""""""""
Campos: ID_USUARIO_CHAT; ID_USUARIO; ID_CHAT; DATA_LOGIN; DATA_LOGOFF; TEMPO_PARTICIPACAO; DATA_ULTIMA_MSG; QUANTIDADE_MENSAGENS;
"""""""""

def filtroFactUsuarioChat():
    collection_usuarios = mongoConnection()['rocketchat']['users'].find()
    collection_rooms_chat = mongoConnection()['rocketchat']['rocketchat_room'].find()
    collection_message = mongoConnection()['rocketchat']['rocketchat_message']
    id_usuario_chat = 0
    vetor_usuario_mensagens_room = []
    for roomChat in collection_rooms_chat:
        for usuario in collection_usuarios:
            mensagens_usuario = list(collection_message.find({'u._id': usuario['_id'], 'rid': roomChat['_id']}))
            #PRIMEIRA MENSAGEM; ULTIMA MENSAGEM, TEMPO DURACAO; DA ROOM SELECIONADA NO USUÁRIO SELECIONADO
            if mensagens_usuario != []:
                id_usuario_chat = id_usuario_chat + 1
                print(mensagens_usuario[0])
                data_login = mensagens_usuario[0]['ts']
                data_logoff = mensagens_usuario[-1]['ts']
                tempo_participacao = (data_logoff - data_login).total_seconds() / 60
                tempo_participacao = "{:.2f}".format(tempo_participacao)
                # QUANTIDADE DE MENSAGENS
                quantidade_mensagens = len(mensagens_usuario)
                linha_vetor = [id_usuario_chat, usuario['_id'], roomChat['_id'], data_login, data_logoff,
                               tempo_participacao, data_logoff, quantidade_mensagens]
                vetor_usuario_mensagens_room.append(linha_vetor)

    #print("Vetor: ", vetor_usuario_mensagens_room)
    return vetor_usuario_mensagens_room


filtroFactUsuarioChat()