from mongoConnection import mongoConnection

from insertsFiltroGiovanni import insertFactChat, insertFactUsuarioChat, insertDimCurso, insertDimDisciplina, insertDimAula, insertFactAcesso

from datetime import datetime

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
    collection_usuarios = mongoConnection()['Logs']['Usuario'].find()
    collection_message = mongoConnection()['rocketchat']['rocketchat_message']
    id_usuario_chat = 0
    for usuario in collection_usuarios:

        mensagens_usuario = list(collection_message.find({'username': usuario['USERNAME']}))
        #print("mensagens_usuario: ", mensagens_usuario)
        #PRIMEIRA MENSAGEM; ULTIMA MENSAGEM, TEMPO DURACAO; DA ROOM SELECIONADA NO USUÁRIO SELECIONADO
        salas = ["GENERAL", "SALA2", "SALA1"]

        for sala in salas:
            print("Sala: ", sala)
            vetor_mensagensPorSalaUsuario = []
            for mensagemUsuario in mensagens_usuario:
                print("SalamensagemUsuario: ", mensagemUsuario['rid'])

                if mensagemUsuario['rid'] == sala:
                    vetor_mensagensPorSalaUsuario.append(mensagemUsuario)
                else:
                    None

            if vetor_mensagensPorSalaUsuario != []:
                print("Teste vetor_mensagensPorSalaUsuario: ", vetor_mensagensPorSalaUsuario)
                id_usuario_chat = id_usuario_chat + 1
                data_login = datetime.strptime(vetor_mensagensPorSalaUsuario[0]['_updateAt'], '%d-%m-%Y %H:%M:%S')
                data_logoff = datetime.strptime(vetor_mensagensPorSalaUsuario[-1]['_updateAt'], '%d-%m-%Y %H:%M:%S')
                tempo_participacao = (data_logoff - data_login).total_seconds() / 60
                tempo_participacao = "{:.2f}".format(tempo_participacao)
                # QUANTIDADE DE MENSAGENS
                quantidade_mensagens = len(vetor_mensagensPorSalaUsuario)

                print("data_login: ", data_login)
                print("data_logoff: ", data_logoff)
                print("tempo_participacao: ", tempo_participacao)
                print("quantidade_mensagens: ", quantidade_mensagens)
                print("sala: ", vetor_mensagensPorSalaUsuario[0]['rid'])
                insertFactUsuarioChat(id_usuario_chat, usuario['IDUSUARIO'], vetor_mensagensPorSalaUsuario[0]['rid'],
                                      data_login, data_logoff, quantidade_mensagens, data_logoff, tempo_participacao)


# CRIAR FILTRO PARA ALIMENTAR TABELA FACT_ACESSO

"""""""""
Campos: ID_USUARIO; ORIGEM; DATA_LOGIN; DATA_LOGOFF;
"""""""""

def dataHoraLogout(datetimeLogin, listLogoutUser):
    vetor = []
    for logoutUser in listLogoutUser:
        if logoutUser['DateTime'] > datetimeLogin:
            linha = logoutUser['DateTime']
            vetor.append(linha)
    if vetor != []:
        menorDatetimeLogout = min(vetor)
        return menorDatetimeLogout
    else:
        menorDatetimeLogout = 0
        return menorDatetimeLogout

def filtroFactAcesso():

    collection_login = mongoConnection()['Logs']['Login']

    for loginLogout in collection_login.find():
        all_login_user = list(collection_login.find({'iduser': loginLogout['iduser'], 'funcao': 'Login'}))
        all_logout_user = list(collection_login.find({'iduser': loginLogout['iduser'], 'funcao': 'Logout'}))

        for login_user in all_login_user:
            data_login = login_user['DateTime']
            data_logoff = dataHoraLogout(data_login, all_logout_user)

        insertFactAcesso(loginLogout['iduser'], data_login, data_logoff, 'P')
        insertFactAcesso(loginLogout['iduser'], data_login, data_logoff, 'C')





#EXECUÇÃO DAS FUNÇÕES DE FILTRO E INSERÇÃO
#filtroFactAcesso()

filtroFactUsuarioChat()





