
import psycopg2


from datetime import date

def conexaoBanco():
    conexao = psycopg2.connect(host='157.245.243.16',
                           port='5432',
                           database='PROJETO_API_NEMO',
                           user='username',
                           password='password')
    return conexao

################################################################# DELETE DATA IN TABLES #################################################################

def deleteDataTables():
    deleteFromDimCurso()


def deleteFromDimCurso():
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM DIM_CURSO CASCADE")
        connection.commit()
        return "DIM_CURSO: DADOS EXCLUIDOS COM SUCESSO"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "DIM_CURSO: NÃO FOI POSSÍVEL EXCLUIR DADOS"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
#deleteDataTables()
################################################################# INSERT DIM CURSO #################################################################
def insertDimCurso():
    collection_curso = filtroDimCurso()
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        for curso in collection_curso:
            comando_insert = """ INSERT INTO dim_curso (id_curso, descricao, graduacao, duracao) VALUES (%s,%s,%s,%s)"""
            values = (curso['idcurso'], curso['descricao'],curso['graduacao'],curso['duracao'])
            cursor.execute(comando_insert, values)
            connection.commit()
            print("INSERT CURSO OK: ", values)
        return "Cursos inseridos com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar cursos!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#EXECUÇÃO DA FUNÇÃO
#insertDimCurso()

##########################################################################################################################################################

################################################################# INSERT DIM AULA #################################################################
def insertDimAula():
    collection_aula = filtroDimAula()
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        for aula in collection_aula:
            #duracao = (aula['dateFim'] - aula['DateInicio']).total_seconds() / 60
            comando_insert = """ INSERT INTO dim_aula (id_aula, data_inicio, data_fim, id_disciplina, titulo, duracao, assunto) VALUES (%s,%s,%s,%s,%s, %s, %s)"""
            values = (aula['idAula'], aula['DateInicio'],aula['dateFim'],aula['idDisciplina'],aula['Titulo'], 10, aula['Assunto'])
            cursor.execute(comando_insert, values)
            connection.commit()
            print("INSERT AULA OK: ", values)
        return "Aulas inseridos com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar aulas!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#EXECUÇÃO DA FUNÇÃO
#insertDimAula()

##########################################################################################################################################################



################################################################# INSERT DIM DICIPLINA #################################################################
def insertDimDisciplina():
    collection_disciplina = filtroDimDisciplina()
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        for disciplina in collection_disciplina:
            comando_insert = """ INSERT INTO dim_disciplina (id_disciplina, id_curso, descricao, id_turma) VALUES (%s,%s,%s,%s)"""
            values = (disciplina['idDisciplina'], disciplina['idcurso'],disciplina['descricao'],disciplina['idturma'])
            cursor.execute(comando_insert, values)
            connection.commit()
        print("INSERT DISCIPLINA OK: ", values)
        return "Disciplinas inseridas com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar disciplinas!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#EXECUÇÃO DA FUNÇÃO
#insertDimDisciplina()

##########################################################################################################################################################


################################################################# INSERT FACT ACESSO #################################################################
def insertFactAcesso(id_usuario, data_login, data_logoff, origem):
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO fact_acesso (id_usuario, data_login, data_logoff, origem) VALUES (%s,%s,%s,%s)"""
        values = (id_usuario, data_login, data_logoff, origem)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT FACT ACESSO OK: ", values)
        return "Acesso inserido com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar acessos!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


##########################################################################################################################################################

################################################################# INSERT FACT CHAT - DIM CHAT(NO BANCO ESTÁ ASSIM) #################################################################
def insertFactChat():
    vetor_chat = filtroFactChat()
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        for chat in vetor_chat:
            comando_insert = """ INSERT INTO dim_chat (id_chat, data_inicio, data_fim, quantidade_usuario, descricao, duracao) VALUES (%s,%s,%s,%s, %s, %s)"""
            values = (chat[0], chat[1],chat[2],chat[3],chat[4],chat[5])
            cursor.execute(comando_insert, values)
            connection.commit()
        print("INSERT FACT CHAT OK: ", values)
        return "Chat inseridos com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar chat!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##########################################################################################################################################################

################################################################# INSERT FACT USUARIO CHAT #################################################################

def insertFactUsuarioChat(id_usuario_chat, id_usuario, id_chat, data_login, data_logoff, quantidade_mensagens, data_ultima_msg, tempo_participacao):
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO fact_usuario_chat (id_usuario_chat, id_usuario, id_chat, data_login, data_logoff, quantidade_mensagens, data_ultima_msg, tempo_participacao) VALUES (%s,%s,%s,%s, %s, %s, %s, %s)"""
        values = (id_usuario_chat, id_usuario, id_chat, data_login, data_logoff, quantidade_mensagens, data_ultima_msg,
                  tempo_participacao)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT FACT USUARIO CHAT OK: ", values)
        return "Usuario Chat inserido com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar usuario chat!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
##########################################################################################################################################################

