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