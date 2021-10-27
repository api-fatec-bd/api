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
